from django.test import TestCase
from .models import Profile,Location,Event,Category

# Create your tests here.
"""
Initializing Category Test Class

"""
class CategoryTestClass(TestCase):
    def setUp(self):
        self.new_category = Category(category_name = 'Food',category_description = 'Everything great and sweet!')
        self.new_category.save()
    def test_instance(self):
        self.assertTrue(isinstance(self.new_category,Category))
    def test_save_method(self):
        self.new_category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)
    def test_delete_method(self):
        self.new_category.save_category()
        categories = Category.objects.all()
        self.new_category.delete_category()
        self.assertTrue(len(categories)==0)
    def test_update_method(self):
        self.new_category.save_category()
        self.new_category.update_category(self.new_category.id, 'Music' ,'Great Music')
        category = Category.objects.filter(category_name='Music',category_description='Great Music').all()
        self.assertTrue(len(category)==1)
    # def test_search_category_by_name(self):
    #     find_cat = self.new_category.search_by_name('Food')
    #     self.assertTrue(len(find_cat)==1)

"""
Initializing Event Test Class

"""
class EventTestClass(TestCase):
    def setUp(self):
        self.new_event = Event(event_title='test event',event_image='form/image.jpg',event_description='event testing',event_location='somewhere',number_of_tickets='50',event_type='eventful',event_topic='event event')
        self.new_event.save()
    def test_instance(self):
        self.assertTrue(isinstance(self.new_event,Event))
    def test_save_method(self):
        self.new_event.save_event()
        events = Event.objects.all()
        self.assertTrue(len(events)>0)
    def test_delete_method(self):
        self.new_event.save_event()
        events = Event.objects.all()
        self.new_event.delete_event()
        self.assertTrue(len(events)==0)
    def test_update_method(self):
        self.new_event.save_event()
        self.new_event.update_event(self.new_event.id,'Me','form/img.png','testing me','someplace','10','business','me business')
        event = Event.objects.filter(event_title='Me',event_image='form/img.png',event_description='testing me',event_location='someplace',number_of_tickets='10',event_type='business',event_topic='me business')
        self.assertTrue(len(event)==1)
