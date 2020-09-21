from django.contrib import admin

from .models.address import Address
from .models.polling_location import PollingLocation
from .models.user import User
from .models.wait_time import WaitTime


# Register your models here.
admin.site.register(Address)
admin.site.register(PollingLocation)
admin.site.register(User)
admin.site.register(WaitTime)
