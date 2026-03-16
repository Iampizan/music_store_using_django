from django.shortcuts import render
from .models import Album

def home_page(request):
    return render(request, 'album/home.html')
def album_listing(request):
    albums = Album.objects.select_related('artist').order_by('-release_date')
    return render(request, 'album/album_list.html', {'albums': albums})