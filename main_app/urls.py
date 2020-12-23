from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/signup/vintner', views.VintnerSignUpView.as_view(), name='vintner_signup'),
    path('accounts/signup/enthusiast', views.EnthusiastSignUpView.as_view(), name='enthusiast_signup'),
    path('glossary/', views.glossary, name='glossary'),
    path('profile/', views.profile, name='profile'),

    ### Winery ###
    path('findwineries/', views.find_wineries, name='find_wineries'),
    path('winery/create/', views.create_winery, name='winery_create'),
    path('winery/<int:winery_id>', views.winery_detail, name="winery_detail"),
    path('winery/<int:winery_id>/update/', views.winery_update, name='winery_update'),
    path('winery/<int:pk>/delete/', views.WineryDelete.as_view(), name='winery_delete'),
    path('winery/search', views.winery_search, name="winery_search"),
    ### Wines ###
    path('findwines/', views.home, name='home'),
    path('mywines/', views.my_wines, name='my_wines'),
    path('wine/<int:pk>/', views.WineDetail.as_view(), name='wine_detail'),
    path('winery/<int:winery_id>/add_wine/', views.create_wine, name='add_wine'),
    path('wine/<int:wine_id>/update/', views.wine_update, name='wine_update'),
    path('wine/<int:pk>/delete/', views.WineDelete.as_view(), name='wine_delete'),
    path('wine/search', views.wine_search, name="wine_search"),
    path('wine/mapsearch', views.wine_search_map, name="wine_search_map"),
    ### Grapes ###
    path('mygrapes/', views.my_grapes, name='my_grapes'),
    ### Comments ###
    path('wine/<int:wine_id>/add_comment/', views.create_comment, name='add_comment'),
    path('comment/<int:pk>/update/', views.CommentUpdate.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDelete.as_view(), name='comment_delete'),
]