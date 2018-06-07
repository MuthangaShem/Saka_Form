from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from location_field.models.plain import PlainLocationField

# Create your models here.
"""
Initializing Category Model

"""
class Category(models.Model):
    category_name = models.CharField(max_length=60)
    category_description = models.TextField(null= True)

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls,id,name,description):
        cls.objects.filter(id=id).update(category_name=name,category_description=description)

    # @classmethod
    # def search_by_name(cls,cat):
    #     category = cls.objects.filter(id__category_name__icontains=cat)
    #     return category
"""
Initializing Event Model

"""
class Event(models.Model):
    event_title = models.CharField(max_length=60)
    event_image = models.ImageField(upload_to = 'pics/',null=True)
    event_description = models.TextField()
    event_location = models.CharField(max_length=60)
    number_of_tickets = models.IntegerField()
    event_type = models.CharField(max_length=60)
    event_topic = models.CharField(max_length=60)

    def __str__(self):
        return self.event_title

    def save_event(self):
        self.save()

    def delete_event(self):
        self.delete()

    @classmethod
    def update_event(cls,id,title,image,description,location,tickets,topic,type):
        cls.objects.filter(id=id).update(event_title=title,event_image=image,event_description=description,event_location=location,number_of_tickets=tickets,event_topic=topic,event_type=type)

"""
Initializing Profile Model

"""
class Profile(models.Model):
    user_profile = models.OneToOneField(User)
    category = models.ForeignKey('Category', related_name = 'interests' , null=True)
    name= models.CharField(max_length=80)
    email= models.CharField(max_length=100)
    location = models.ForeignKey('Location', related_name='area',null=True)

"""
Initializing Location Model

"""

class Location(models.Model):
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
