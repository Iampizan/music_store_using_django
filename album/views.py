from django.shortcuts import render, get_object_or_404
from .models import Album

def home_page(request):
    return render(request, 'album/home.html')


def album_listing(request):
    albums = Album.objects.select_related('artist').order_by('-release_date')
    return render(request, 'album/album_list.html', {'albums': albums})


def album_details(request, album_id):
    albums = Album.objects.select_related('artist')
    album = get_object_or_404(Album, id=album_id)
    return render(request, "album/album_detail.html", {'album': album, 'albums': albums})