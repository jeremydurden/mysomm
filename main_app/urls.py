from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('glossary/', views.glossary, name='glossary'),
    path('profile/', views.profile, name='profile'),

    ### Winery ###
    path('findwineries/', views.find_wineries, name='find_wineries'),
    path('winery/create/', views.create_winery, name='winery_create'),
    path('winery/<int:winery_id>', views.winery_detail, name="winery_detail"),
    ### Wines ###
    path('findwines/', views.home, name='home'),
    path('mywines/', views.my_wines, name='my_wines'),
    path('wines/<int:pk>/', views.WineDetail.as_view(), name='wines_detail'),
    path('winery/<int:winery_id>/add_wine/', views.create_wine, name='add_wine'),


    ### Grapes ###
    path('mygrapes/', views.my_grapes, name='my_grapes'),
]