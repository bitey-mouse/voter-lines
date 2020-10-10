from decimal import Decimal

#from generic_relations.relations import GenericRelatedField
from rest_framework import serializers
from rest_framework.response import Response

from .google_civic import GoogleCivic
from .models.address import Address
from .models.polling_location import PollingLocation
from .models.user import User
from .models.wait_time import WaitTime


class BaseModelSerializer(serializers.ModelSerializer):
    object_type = serializers.SerializerMethodField()

    def get_object_type(serializer, model):
        return model.__class__.__name__.lower()


class AddressSerializer(serializers.ModelSerializer):
    # object_with_address = GenericRelatedField({
    #     PollingLocation: PollingLocationSerializer(),
    #     User: UserSerializer()
    # })
    class Meta:
        model = Address
        fields = ('id', 'street1', 'street2', 'city', 'state', 'zip_code', 'latitude', 'longitude')


class PollingLocationSerializer(BaseModelSerializer):
    address = AddressSerializer(required=True)
    
    class Meta:
        model = PollingLocation
        #fields = ('id', 'name', 'google_civic_id', 'address')
        fields = '__all__'

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        pl = PollingLocation.objects.create(address=address, **validated_data)
        return pl




class UserSerializer(BaseModelSerializer):
    address = AddressSerializer(required=True)
    polling_locations = PollingLocationSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'is_admin', 'address', 'polling_locations')

    # Override the create action to lookup polling locations
    def create(self, validated_data):
        # Grabe user's address
        address_data = validated_data.pop('address')
        address_obj = Address.objects.create(**address_data)
        user = User.objects.create(address=address_obj, **validated_data)

        # Lookup new Address on Google Civic to locate polling locations
        r_json = GoogleCivic.get_voter_info(address_obj)
        if 'error' in r_json:
            #pass
            # TODO:  SOMETHING HERE
            print('**************************** ERROR!!!!')
            print(r_json)

        else:
            ############### TODO:  PARSE/SAVE POLLING LOCATIONS
            print('**************************** SUCCESS!!!!')
            print(r_json)
            if 'pollingLocations' in r_json:
                for pl_json in r_json['pollingLocations']:
                    pl_address_json = pl_json.get('address', {})

                    # Map data from Google Civic response, and append each to polling_location list
                    pl_name = pl_json.get('name', None)
                    if not pl_name:
                        pl_name = pl_address_json.get('locationName', None)


                    pl_data = {
                        'name': pl_name,
                        'google_civic_id': pl_json.get('id', None),
                        'polling_hours': pl_json.get('pollingHours', None),
                        'notes': pl_json.get('notes', None),
                        'start_date': pl_json.get('startDate', None),
                        'end_date': pl_json.get('endDate', None),
                    }

                    pl_address_data = {
                            'street1': pl_address_json.get('line1', ''),
                            'street2': pl_address_json.get('line2', None),
                            'city': pl_address_json.get('city', ''),
                            'state': pl_address_json.get('state', ''),
                            'zip_code': pl_address_json.get('zip', ''),
                            'latitude': pl_json.get('latitude', None),
                            'longitude': pl_json.get('longitude', None)
                        }


                    ## TODO: SEARCH IF POLLING LOCATION MATCH IS FOUND IN DATABASE
                    ###      AND USE IT IF FOUND. IF DNE, THEN CREATE NEW POLLING LOCATION
                    ###   MAYBE MOVE THIS PART TO GoogleCivic class, SINCE WE'LL NEED TO DO THIS
                    ###       DAILY IN A SCRIPT.
                    pl_obj = None

                    # Match by civic_id
                    if pl_data['google_civic_id']:
                        try:
                            pl_obj = PollingLocation.objects.get(google_civic_id=pl_data['google_civic_id'])
                            print(f'PollingLocation match found by google_civic_id:  id={pl_obj.id}')
                        except:
                            pass
                    # Match by coordinates
                    if not pl_obj and (pl_address_data['latitude'] and pl_address_data['longitude'] ):
                        try:
                            pl_obj = PollingLocation.objects.get(
                                address__latitude=pl_address_data['latitude'],
                                address__longitude=pl_address_data['longitude'])
                            print(f'PollingLocation match found by coordinates:  id={pl_obj.id}')
                        #except:
                        except Exception as e:
                            print(e)
                            print(f"LAT: {pl_address_data['latitude']} ==> {Decimal(pl_address_data['latitude'])}")
                            print(f"LON: {pl_address_data['longitude']} ==> {Decimal(pl_address_data['longitude'])}")
                            pass
                    # Match by address
                    if not pl_obj and (
                        pl_address_data['street1'] and pl_address_data['city'] and
                        pl_address_data['state'] and pl_address_data['zip_code'] ):
                        try:
                            pl_obj = PollingLocation.objects.get(
                                address__street1=pl_address_data['street1'],
                                address__city=pl_address_data['city'],
                                address__state=pl_address_data['state'],
                                address__zip_code=pl_address_data['zip_code'])
                            print(f'PollingLocation match found by address:  id={pl_obj.id}')
                        except:
                            pass

                    if not pl_obj:
                        # No prev match found. Must create new one polling location
                        pl_address_obj = Address.objects.create(**pl_address_data)
                        pl_obj = PollingLocation.objects.create(address=pl_address_obj ,**pl_data)
                        print(f'No previous PollingLocation found. Creating new object:  id={pl_obj.id}')
                      

                    user.polling_locations.add(pl_obj)
        return user


class WaitTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitTime
        fields = ('id', 'polling_location', 'start_time', 'end_time', 
            'total_time_hours', 'total_time_mins')
