from django.contrib import admin
from .models import *
from mapwidgets.widgets import GooglePointFieldWidget
from django.contrib.gis.db import models

admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(TicketBooking)


class Event(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }
