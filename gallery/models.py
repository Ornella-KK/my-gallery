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
    gallery_image = models.ImageField(upload_to = 'pictures/')
    title = models.CharField(max_length =60)
    description = models.TextField()
    category = models.ForeignKey(Category)
    address = models.ForeignKey(Location)
    pub_date = models.DateTimeField(auto_now_add=True)