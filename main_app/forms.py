from django import forms

class CreateWineryForm(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    region = forms.CharField(max_length=100)
    county = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=2)
    zipcode = forms.CharField(max_length=5)
    img_url = forms.CharField(max_length=100)
    logo_url = forms.CharField(max_length=100)