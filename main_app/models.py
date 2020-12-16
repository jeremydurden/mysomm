from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Winery(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    img_url = models.CharField(max_length=100)
    logo_url = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} is located at {self.address} in {self.city}, {self.state}'
    


class Wine(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    varietal = models.CharField(max_length=100)
    vintage = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    taste_notes = models.TextField(max_length=250)
    image_url = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} is a {self.vintage} {self.style} wine.'
    
class Grape(models.Model):
    name = models.CharField(max_length=100)
    sci_name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} has a scientific name of {self.sci_name}'