import requests

from os import environ
from simplejson.errors import JSONDecodeError

from .models.address import Address

class GoogleCivic():

    @staticmethod
    def get_voter_info(address_obj: Address):
        # Gather auth keys and ids
        try:
            env_key = environ['GOOGLE_CIVIC_API_KEY']
        except KeyError:
            env_key = None
        if not env_key:
            raise ValueError("No 'GOOGLE_CIVIC_API_KEY' found in environment variables. Please set this value and retry.")
        
        try:
            election_id = environ['GOOGLE_CIVIC_ELECTION_ID']
        except KeyError:
            election_id = None
        if not election_id:
            election_id = 7000  # Default to id for November 2020 US General Election
        
        # Setup querystring parameters
        payload = {
            'key': env_key,
            'electionId': election_id,
            'address': address_obj.url_string()
        }

        # Send the request
        r = requests.get('https://civicinfo.googleapis.com/civicinfo/v2/voterinfo', params=payload)

        # Google Civic will either return a JSON with successful query-data, or return a detailed error message in JSON form, 
        #     so only throw exception here if no JSON message is returned from Google.  
        try:
            r_json = r.json()
        except JSONDecodeError:
            r_json = {}

        if not r_json:
            r.raise_for_status()
        return r_json
