from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    ### Winery ###
    path('findwineries/', views.find_wineries, name='find_wineries'),
    path('winery/create/', views.create_winery, name='winery_create'),
    path('/winery/<int:winery_id>', views.winery_detail, name="winery_detail"),
    ### Wine ###
    path('findwines/', views.find_wines, name='find_wines'),
    path('mywines/', views.my_wines, name='my_wines'),
    ### Grape ###
    path('mygrapes/', views.my_grapes, name='my_grapes'),

]