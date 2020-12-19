from django.db import models

class Category(models.Model):
    title = models.CharField(max_length =30)

class Location(models.Model):
    name = models.CharField(max_length =30)