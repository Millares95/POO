from django.db import models

class SuperHeroes(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    accesorio = models.CharField(max_length=100)
