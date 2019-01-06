from django.db import models
from datetime import datetime
from django.urls import reverse_lazy

# Create your models here.
class pet(models.Model):
    description = models.TextField()
    lng = models.DecimalField(max_digits = 9, decimal_places = 6)
    lat = models.DecimalField(max_digits = 9, decimal_places = 6)
    date_published = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to = 'pet_pics/', default = 'pet_pics/None/no-img.jpg')

    def __str__(self):
        return f'{self.description} {self.date_published} {self.lng} {self.lat} {self.image}'
   
    def get_absolute_url(self):
        return reverse_lazy('post_created', args=[str(self.id)])