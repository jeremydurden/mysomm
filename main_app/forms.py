from django import forms
from django.forms import ModelForm
from .models import Wine, Winery, Comment
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

class WineryForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    region = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    county = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'class': 'form-control'}))
    zipcode = forms.CharField(max_length=5, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    img_url = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    logo_url = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))



class WineForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    style = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    grape = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    vintage = forms.CharField(max_length=4, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    color = forms.ChoiceField(choices=Wine.COLOR_CHOICES, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    taste_notes = forms.CharField(max_length=250, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    image_url = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

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
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name']
        field_order = ['username', 'password', 'first_name', 'last_name']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_vintner = True
        if commit:
            user.save()
        return user

class EnthusiastSignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name']
        field_order = ['username', 'password', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_enthusiast = True
        if commit:
            user.save()
        return user

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['content', 'rating']