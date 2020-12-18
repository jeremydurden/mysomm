from django import forms
from django.forms import ModelForm
from .models import Wine, Winery

class WineryForm(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    region = forms.CharField(max_length=100)
    county = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=2)
    zipcode = forms.CharField(max_length=5)
    img_url = forms.CharField(max_length=100)
    logo_url = forms.CharField(max_length=100)



class WineForm(ModelForm):
    class Meta:
        model = Wine
        fields = ['name', 'style', 'grape', 'vintage', 'color', 'taste_notes', 'image_url']

