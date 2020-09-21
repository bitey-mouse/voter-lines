from django.shortcuts import render
from rest_framework import viewsets

from .models.address import Address
from .models.polling_location import PollingLocation
from .models.user import User
from .models.wait_time import WaitTime
from .serializers import (
    AddressSerializer, 
    PollingLocationSerializer,
    UserSerializer,
    WaitTimeSerializer)


class AddressViewSet(viewsets.ModelViewSet):
    #queryset = Hero.objects.all().order_by('name')
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class PollingLocationViewSet(viewsets.ModelViewSet):
    #queryset = Hero.objects.all().order_by('name')
    queryset = PollingLocation.objects.all()
    serializer_class = PollingLocationSerializer


class UserViewSet(viewsets.ModelViewSet):
    #queryset = Hero.objects.all().order_by('name')
    queryset = User.objects.all()
    serializer_class = UserSerializer


class WaitTimeViewSet(viewsets.ModelViewSet):
    #queryset = Hero.objects.all().order_by('name')
    queryset = WaitTime.objects.all()
    serializer_class = WaitTimeSerializer