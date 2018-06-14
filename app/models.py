<<<<<<< HEAD

=======
>>>>>>> 0dc7e00b9902c6ec5425bace5c6e33b3e64bd9de
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
<<<<<<< HEAD
=======
from django.core.validators import RegexValidator
>>>>>>> 0dc7e00b9902c6ec5425bace5c6e33b3e64bd9de
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

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls, id, name, description):
        cls.objects.filter(id=id).update(category_name=name, category_description=description)


class Profile(models.Model):
    """
    Initializing Profile Model
    """
    profile_owner = models.OneToOneField(User)
    profile_interest = models.ForeignKey('Category', related_name='interests', null=True)
    profile_name = models.CharField(max_length=80)
<<<<<<< HEAD
    profile_email = models.CharField(max_length=100)
=======

    def __str__(self):
        return self.profile_owner.username


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(profile_owner=instance)
        instance.profile.save()
>>>>>>> 0dc7e00b9902c6ec5425bace5c6e33b3e64bd9de


class Event(models.Model):
    """
    Initializing Event Model
    """
<<<<<<< HEAD
    event_title = models.CharField(max_length=60)
    event_image = models.ImageField(upload_to='event-images/', null=True)
    event_description = models.TextField()
    event_location = models.CharField(max_length=60)
    number_of_tickets = models.IntegerField()
    event_type = models.CharField(max_length=60)
    event_topic = models.CharField(max_length=255)
=======
    event_owner = models.ForeignKey('Profile')
    event_title = models.CharField(max_length=60)
    event_image = models.ImageField(upload_to='events/', blank=True, null=True)
    event_type = models.CharField(max_length=60, blank=True, null=True)
    event_category = models.ForeignKey('Category', null=True, blank=True)
    event_description = models.TextField()
    event_location = models.CharField(max_length=60)
    number_of_tickets = models.CharField(max_length=8,
                                         validators=[
                                             RegexValidator(
                                                 regex=r'^(\d{1,5})$',
                                                 message='Please enter a valid ticket number'
                                             ),
                                         ])
    event_date = models.DateTimeField(null=True, blank=True)
    event_created_on = models.DateTimeField(auto_now_add=True,  null=True, blank=True)
>>>>>>> 0dc7e00b9902c6ec5425bace5c6e33b3e64bd9de

    def __str__(self):
        return self.event_title

    def save_event(self):
        self.save()

    def delete_event(self):
        self.delete()

<<<<<<< HEAD
    # @classmethod
    # def update_event(cls, id, **kwargs):
    #     cls.objects.filter(id=id).update(event_title=kwargs['event_title'], event_image=kwargs['event_image'], event_description=kwargs['event_description'],
    #                                      event_location=kwargs['event_location'], number_of_tickets=kwargs['number_of_tickets'], event_type=kwargs['event_type'], event_topic=kwargs['event_topic'])
=======
    class Meta:
        ordering = ['-event_created_on']
>>>>>>> 0dc7e00b9902c6ec5425bace5c6e33b3e64bd9de
