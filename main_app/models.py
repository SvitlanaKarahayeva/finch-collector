from django.db import models
from django.db.models.fields import IntegerField
from django.urls import reverse

# Create your models here.

FOODS = (
    (1, 'Nyjer Seed'),
    (2, 'Sunflower Seeds'),
    (3, 'White Proso Millet'),
    (4, 'Rapeseed Seeds'),
    (5, 'Canary Seeds'),
    (6, 'Shelled And Cracked Corn')
)

class Park(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('parks_detail', kwargs={ 'pk': self.id })

class Finch(models.Model):
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    size = models.IntegerField()

    def __str__(self):
        return self.breed

    def get_absolute_url(self):
        return reverse('detail', kwargs={ 'finch_id': self.id })

class Feeding(models.Model):
    date = models.DateField('feeding date')
    food = IntegerField(
        choices=FOODS,
        default=FOODS[1][0]
    )
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_food_display()} on {self.date}'

    class Meta:
        ordering = ['-date']