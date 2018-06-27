from django.contrib import admin
from .models import *
from django.contrib.gis.db import models

admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(TicketBooking)


