from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from location_field.models.plain import PlainLocationField


class Category(models.Model):
    """
    Initializing Category Model
    """
    category_name = models.CharField(max_length=60)
    category_description = models.TextField(null=True)

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()
