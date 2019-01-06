from django.db import models

# Create your models here.

class nasa_models(models.Model):
    rating = models.IntegerField()
    favorite = models.BooleanField()
    comment = models.TextField()
    date = models.DateField()
    url = models.URLField()
