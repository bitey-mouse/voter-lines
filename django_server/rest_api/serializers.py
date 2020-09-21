from rest_framework import serializers
from generic_relations.relations import GenericRelatedField

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
        fields = ('id', 'name', 'google_civic_id', 'address')

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        pl = PollingLocation.objects.create(address=address, **validated_data)
        return pl


class UserSerializer(BaseModelSerializer):
    address = AddressSerializer(required=True)
    polling_locations = PollingLocationSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ('id', 'is_admin', 'address', 'polling_locations')

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        user = User.objects.create(address=address, **validated_data)
        return user


class WaitTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitTime
        fields = ('id', 'polling_location', 'start_time', 'end_time', 
            'total_time_hours', 'total_time_mins')
