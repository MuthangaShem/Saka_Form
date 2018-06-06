from django.test import TestCase
from .models import Category


class CategoryTestClass(TestCase):
    """
    Initializing Category Test Class
    """

    def setUp(self):
        self.new_category = Category(
            category_name='Food', category_description='Everything great and sweet!')

    def test_category_instance_true(self):
        self.assertTrue(isinstance(self.new_category, Category))

    def test_save_category_method_true(self):
        self.new_category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 1)

    def test_delete_category_method_true(self):
        self.new_category.save_category()
        categories = Category.objects.all()
        self.new_category.delete_category()
        self.assertTrue(len(categories) == 0)
