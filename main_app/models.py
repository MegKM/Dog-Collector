from django.db import models
from django.urls import reverse

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    age = models.IntegerField()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})

    def __str__(self):
        return f"{self.name}"
