from django.test import TestCase
from .models import Category,Location,Image

class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.happiness= Category(title = 'Happiness')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.happiness,Category))

    # Testing Save Method
    def test_save_method(self):
        self.happiness.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.kigali= Location(place = 'Kigali')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kigali,Location))

    # Testing Save Method
    def test_save_method(self):
        self.kigali.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

