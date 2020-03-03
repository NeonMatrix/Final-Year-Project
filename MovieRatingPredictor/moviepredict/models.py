from django.db import models

class PredictedMovie(models.Model):
    budget = models.IntegerField(default=0)
    runtime = models.IntegerField(default=0)
