from django.db import models

# Create your models here.


class DogImage(models.Model):
    url = models.CharField(max_length=400)
    