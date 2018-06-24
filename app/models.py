from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator


class Category(models.Model):
    """
    Initializing Category Model
    """
    category_name = models.CharField(max_length=60)
    category_image = models.ImageField(upload_to='category-images')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'categories'

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
    profile_interest = models.ManyToManyField('Category', related_name='interests', null=True)
    profile_name = models.CharField(max_length=80, blank=True, null=True)
    profile_location = models.CharField(max_length=254, null=True)

    def __str__(self):
        return self.profile_owner.username


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    u_location = getattr(instance, '_location', None)
    if created:
        Profile.objects.create(profile_owner=instance, profile_location=u_location)
        instance.profile.save()


class Event(models.Model):
    """
    Initializing Event Model
    """
    EVENT_CHOICES = (
        ('F', 'FREE'),
        ('P', 'PAID'),
    )
    event_owner = models.ForeignKey('Profile')
    event_title = models.CharField(max_length=60)
    event_image = models.ImageField(upload_to='events/', blank=True, null=True)
    event_category = models.ForeignKey('Category')
    event_status = models.CharField(max_length=2, choices=EVENT_CHOICES)
    event_charges = models.CharField(max_length=8, null=True, validators=[RegexValidator(
        regex=r'^(\d{1,5})$', message='Enter a valid amount'), ])
    event_description = models.TextField()
    event_location = models.CharField(max_length=60)
    number_of_tickets = models.CharField(max_length=8, validators=[RegexValidator(
        regex=r'^(\d{1,5})$', message='Enter a valid number'), ])
    event_date = models.DateTimeField(null=True, blank=True)
    event_created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_title

    def save_event(self):
        self.save()

    def delete_event(self):
        self.delete()

    def ticket_count(self):
        return self.eventticket_set.filter(event_ticket_taken=False).count()

    class Meta:
        ordering = ['-event_created_on']


class TicketBooking(models.Model):
    """
    Initializing TicketBooking Model
    """
    profile = models.ForeignKey('Profile')
    event = models.ForeignKey('Event')
    profile_idf = models.CharField(max_length=8, verbose_name="Identification Number",
                                   validators=[RegexValidator(regex=r'^(\d{7}|\d{8})$', message='ID number must be numeric and eight characters'), ])
    profile_phone = models.CharField(max_length=15, validators=[RegexValidator(
        regex=r'^(0+[7]{1}[0-9]{8})$', message='Incorrect Phone Number'), ], verbose_name='Phone Number')
    number_of_tickets = models.CharField(max_length=8, validators=[RegexValidator(
        regex=r'^(\d{1,5})$', message='Enter a valid number'), ])
    ticket_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.event.event_title


class EventTicket(models.Model):
    """
    Initializing EventTicket Model
    """
    event = models.ForeignKey('Event')
    event_booking = models.ForeignKey('TicketBooking', null=True)
    event_ticket_no = models.CharField(max_length=50, unique=True)
    event_ticket_taken = models.BooleanField(default=False)

    def __str__(self):
        return self.event_ticket_no
