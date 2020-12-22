from django.db import models
from django.contrib.auth.models import  AbstractUser

from django.urls import reverse


class User(AbstractUser):
    is_vintner = models.BooleanField(default=False)
    is_enthusiast = models.BooleanField(default=False)

class Vintner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Enthusiast(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)




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
    zipcode = models.CharField(max_length=5, null=True)
    img_url = models.CharField(max_length=100, null=True)
    logo_url = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} is located at {self.address} in {self.city}.'
    

class Wine(models.Model):
    RED = 'RD'
    WHITE = 'WH'
    ROSE = 'RS'
    COLOR_CHOICES = [
        ('', 'Color'), ## Allows for blanks in search and dropdowns
        (RED, 'Red'),
        (WHITE, 'White'),
        (ROSE, 'Rosé'),
    ]

    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100, null=True)
    grape = models.CharField(max_length=100, null=True)
    vintage = models.CharField(max_length=4, null=True)
    color = models.CharField(max_length=5, choices=COLOR_CHOICES, default=RED, null=True)
    taste_notes = models.TextField(max_length=250, null=True)
    image_url = models.CharField(max_length=100, null=True)
    winery = models.ForeignKey(Winery, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} is a {self.vintage} {self.style} wine.'

    def get_absolute_url(self):
        return reverse('winery_detail', kwargs={'winery_id': self.winery.id})

    
class Grape(models.Model):
    name = models.CharField(max_length=100)
    sci_name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} has a scientific name of {self.sci_name}'

class Comment(models.Model):
    
    SCORES = [
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    ]

    content = models.TextField(max_length=250, null=True)
    rating = models.TextField(choices=SCORES, default=SCORES[0][0])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.rating} is the rating on this comment'
    
    def get_absolute_url(self):
        return reverse('wine_detail', args={self.wine.id})