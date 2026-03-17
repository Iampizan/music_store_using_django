from django.shortcuts import render, get_object_or_404
from .models import Artist
from album.models import Album

def artist_list(request):
    artists = Artist.objects.all().order_by('debut_year')
    return render(request, "artist/artist_list.html", { "artists": artists})

def artist_details(request, artist_pk):
    artist = get_object_or_404(Artist, id=artist_pk)
    albums = Album.objects.select_related('artist')
    return render(request, 'artist/artist_details.html', {'artist': artist, 'albums': albums})

