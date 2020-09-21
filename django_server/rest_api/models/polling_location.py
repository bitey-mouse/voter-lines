#from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from .address import Address


class PollingLocation(models.Model):
    
    name = models.CharField(max_length=64)
    google_civic_id = models.PositiveIntegerField(null=True, blank=True)
    #people = db.relationship('User', backref='polling_location', lazy='dynamic')
    #wait_times = db.relationship('WaitTime', backref='pollingidlocation', lazy='dynamic')
    #address = GenericRelation(Address)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=False, blank=False)
