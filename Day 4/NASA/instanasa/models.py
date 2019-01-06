from django.db import models
from django.urls import reverse_lazy, reverse

# Create your models here.
class instanasa(models.Model):
    comments = models.TextField()
    rating = models.IntegerField()
    favorite = models.BooleanField()
    url = models.URLField()
    date = models.DateField()

    def __str__(self):
        return f'{self.comments} {self.date} {self.rating}'

    def get_absolute_url(self):
        return reverse_lazy('comment_details', args=[str(self.id)])
    