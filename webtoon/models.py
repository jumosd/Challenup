from django.db import models

# Create your models here.


class Webtoon(models.Model):
    penname = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    tag = models.CharField(max_length=20)
    thumbnail = models.CharField(max_length=20)