from django.urls import path
from . import views

app_name = 'artists'

urlpatterns = [
    path('artist/', views.artist_list, name='artist'),
    path('artist/<int:artist_pk>/', views.artist_details, name='artist_details'),
]