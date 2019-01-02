from django.db import models

# Create your models here.

class Kickstarter_camp(models.Model):
    
    backers_count = models.IntegerField()

    blurb = models.TextField()

    goal = models.FloatField()

    pledged = models.FloatField()

    def __str__(self):
        return self.blurb



