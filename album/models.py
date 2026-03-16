from django.db import models
from artists.models import Artist
from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_release_date(value):
    current_year = timezone.now().year
    if value.year < 1800 or value.year > current_year:
        raise ValidationError(f"Release year must be between 1800 and {current_year}.")


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artists')
    title = models.CharField(max_length=100)
    release_date = models.DateField(validators=[validate_release_date])
    cover = models.ImageField(upload_to='albums/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} {self.release_date}"
