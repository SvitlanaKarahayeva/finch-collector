from django.db import models
from django.urls import reverse

# Create your models here.

class Finch(models.Model):
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    size = models.IntegerField()

    def __int__(self):
        return self.breed

    def get_absolute_url(self):
        return reverse('detail', kwargs={ 'finch_id': self.id })
