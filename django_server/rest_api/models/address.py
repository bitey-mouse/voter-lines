from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Address(models.Model):
    street1 = models.CharField(max_length=128)
    street2 = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    latitude = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    # Here is how we relate the foreign-id to both users and polling_locations
    #content_type =   models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
    #object_id = models.PositiveIntegerField()
    #object_with_address=GenericForeignKey('content_type', 'object_id')

    # def __init__(self, zip_code):
    #     if '-' in zip_code:
    #       self.zip_code = zip_code.split('-')[0]
    #     self.zip_code = zip_code


    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    # def __str__(self):
    #     return self.name