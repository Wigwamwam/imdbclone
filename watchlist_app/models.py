from django.db import models
from django.db.models import Model

# Create your models here.

class Movie(Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
