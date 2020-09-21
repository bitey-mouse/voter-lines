#from django import forms
from django.db import models

from .polling_location import PollingLocation


class WaitTime(models.Model):
    polling_location = models.ForeignKey(PollingLocation, on_delete=models.SET_NULL, null=True, blank=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    #total_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), null=True)
    total_time_hours = models.PositiveIntegerField(null=True, blank=True)
    total_time_mins = models.PositiveIntegerField(null=True, blank=True)

    

    def overview(self):
        return {
            "code": 0,
            "total_time": f'{self.total_time_hours}:{self.total_time_mins}',
            "end_time": self.end_time,
            "poll_location_id": self.polling_location.id
        }