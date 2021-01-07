from django.db import models
import datetime as dt


class Category(models.Model):
    title = models.CharField(max_length =30)

    def __str__(self):
        return self.title

    def save_category(self):
        self.save()

class Location(models.Model):
    place = models.CharField(max_length =30)

    def __str__(self):
        return self.place

    def save_location(self):
        self.save()

class Image(models.Model):
    gallery_image = models.ImageField(upload_to = 'pictures/', null =True)
    name = models.CharField(max_length =60)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    address = models.ForeignKey(Location,on_delete = models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @property
    def gallery_image_url(self):
        if self.gallery_image and hasattr(self.gallery_image, 'url'):
            return self.gallery_image.url

    @classmethod
    def search_by_category(cls,search_images):
        gallery = cls.objects.filter(category__title__icontains=search_images)
        return gallery

    @classmethod
    def view_location(cls,place):
        location = cls.objects.filter(location=place)
        return location

    @classmethod
    def view_category(cls,caty):
        category = cls.objects.filter(category=caty)
        return category
    
    