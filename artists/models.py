from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    debut_year = models.IntegerField()
    photo = models.ImageField(upload_to="artists/", blank=True, null=True)


    def __str__(self):
        return f"{self.name} {self.debut_year}"
