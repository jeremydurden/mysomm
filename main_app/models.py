from django.db import models
from django.contrib.auth.models import User





class Profile(models.Model):
    def __str__(self):
        return f'{self}'

class Glossary(models.Model):
    def __str__(self):
        return f'{self}'



class County(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f'{self.name} is in {self.state}'

# Create your models here.
class Winery(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    county = models.ForeignKey(County, on_delete=models.SET_NULL, null=True)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=5)
    img_url = models.CharField(max_length=100)
    logo_url = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} is located at {self.address} in {self.city}.'
    


class Wine(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    varietal = models.CharField(max_length=100)
    vintage = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    taste_notes = models.TextField(max_length=250)
    image_url = models.CharField(max_length=100)
    winery = models.ForeignKey(Winery, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} is a {self.vintage} {self.style} wine.'
    
class Grape(models.Model):
    name = models.CharField(max_length=100)
    sci_name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} has a scientific name of {self.sci_name}'
