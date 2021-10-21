from django.db import models

# Create your models here.

class Finch(models.Model):
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    size = models.IntegerField()

    def __int__(self):
        return self.breed
