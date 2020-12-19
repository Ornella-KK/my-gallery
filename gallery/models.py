from django.db import models

class Category(models.Model):
    title = models.CharField(max_length =30)

    def __str__(self):
        return self.title

class Location(models.Model):
    place = models.CharField(max_length =30)

    def __str__(self):
        return self.place
