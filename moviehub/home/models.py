from django.db import models

class Movie(models.Model):
    name=models.CharField(max_length=20)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    language = models.CharField(max_length=20)
    details = models.CharField(max_length=30)

    def __str__(self):
        return self.name