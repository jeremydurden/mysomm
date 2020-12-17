from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.FindWineIndex.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('mywines/', views.my_wines, name='my_wines'),
    path('mygrapes/', views.my_grapes, name='my_grapes'),
    path('findwines/', views.find_wines, name='find_wines'),
    path('findwineries/', views.find_wineries, name='find_wineries'),
    path('winery/create/', views.WineryCreate.as_view(), name='winery_create'),
]