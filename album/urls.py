from django.urls import path
from . import views

app_name = 'album'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('albums/', views.album_listing, name='album_list'),
]