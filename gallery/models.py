from django.db import models

class Category(models.Model):
    title = models.CharField(max_length =30)

    def __str__(self):
        return self.title

class Location(models.Model):
    place = models.CharField(max_length =30)

    def __str__(self):
        return self.place

class Image(models.Model):
    gallery_image = models.ImageField(upload_to = 'pictures/')
    title = models.CharField(max_length =60)
    description = models.TextField()
    category = models.ForeignKey(Category)
    address = models.ForeignKey(Location)