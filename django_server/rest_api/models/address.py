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

    def __add_if_exists(self, full_s, field, prepend_comma=False):
        if field:
            if prepend_comma:
                full_s += ', ' + field.strip()
            else:
                full_s += ' ' + field.strip()
        return full_s



    def url_string(self):
        s = ''
        s = self.__add_if_exists(s, self.street1)
        s = self.__add_if_exists(s, self.street2)
        s = self.__add_if_exists(s, self.city, True)
        s = self.__add_if_exists(s, self.state, True)
        s = self.__add_if_exists(s, self.zip_code)
        return s

