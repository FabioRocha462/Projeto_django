from django.db import models
from django.contrib.auth.models import User
class Proj(models.Model):
    Nome = models.CharField(max_length=255)
    Tel = models.CharField(max_length=255)
    email = models.CharField(max_length=255) 

    def __str__(self):
        return self.Nome 