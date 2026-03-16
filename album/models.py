from django.db import models
from artists.models import Artist

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artists')
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    cover = models.ImageField(upload_to='albums/', blank=True, null=True)


    def __str__(self):
        return f"{self.title} {self.release_date}"

