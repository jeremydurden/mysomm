from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('mywines/', views.mywines, name='mywines'),
    path('mygrapes/', views.mygrapes, name='mygrapes'),
    path('findwines/', views.findwines, name='findwines'),
    path('findwineries/', views.findwineries, name='findwineries'),
    path('winery/create/', views.WineryCreate.as_view(), name='cats_create'),
]