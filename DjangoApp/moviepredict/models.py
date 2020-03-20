from django.db import models

class Actor(models.Model):
    imdb_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)

class Director(models.Model):
    imdb_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
