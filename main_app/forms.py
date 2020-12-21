from django import forms
from django.forms import ModelForm
from .models import Wine, Winery
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

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


class WineSearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder':'Wine Name', 'class': 'form-control'}))
    style = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder':'Style', 'class': 'form-control'}))
    grape = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder':'Grape', 'class': 'form-control'}))
    min_year = forms.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(9999)], required=False, widget=forms.NumberInput(attrs={'placeholder':'Min Year', 'class': 'form-control'}))
    max_year = forms.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(9999)], required=False, widget=forms.NumberInput(attrs={'placeholder':'Max Year', 'class': 'form-control'}))
    color = forms.ChoiceField(choices=Wine.COLOR_CHOICES, required=False, widget=forms.Select(attrs={'class': 'form-control form-placeholder'}))

class WinerySearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder':'Winery Name', 'class': 'form-control'}))
    region = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder':'Region', 'class': 'form-control'}))
    county = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder':'County', 'class': 'form-control'}))
    state = forms.CharField(max_length=2, required=False, widget=forms.TextInput(attrs={'placeholder':'State', 'class': 'form-control'}))



class VintnerSignUpForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_vintner = True
        if commit:
            user.save()
        return user

class EnthusiastSignUpForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_enthusiast = True
        if commit:
            user.save()
        return user