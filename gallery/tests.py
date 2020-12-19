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

class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.happiness= Category(first_name = 'Happiness')
        self.happiness.save_category()

        # Creating a new tag and saving it
        self.new_location = Location(place = 'kigali')
        self.new_location.save()

        self.new_image= Image(name = 'Living the best life',description = 'This is a random test Post',category = self.happiness)
        self.new_image.save()

        self.new_image.address.add(self.new_location)

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()