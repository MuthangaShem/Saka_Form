from django.contrib import admin
<<<<<<< HEAD
from .models import Category,Event

# Register your models here.
admin.site.register(Event)
=======
from .models import *

admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(EventType)
>>>>>>> ba299aa0c502e58a7c53e3bf18136cf3ad2ccf23
