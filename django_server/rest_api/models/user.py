#from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from .address import Address
from .polling_location import PollingLocation


class User(models.Model):
    polling_locations = models.ManyToManyField(PollingLocation)
    is_admin = models.BooleanField(default=False)
    #address = GenericRelation(Address)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    
    # def __init__(self, polling_location, is_admin):
    #     self.polling_location = polling_location
    #     self.is_admin = is_admin


    # Not sure this is useful... just keep in case
    # def overview(self):
    #     return {
    #         "code": 0,
    #         "poll_id": self.polling_location,
    #         "is_admin": self.is_admin
    #     }