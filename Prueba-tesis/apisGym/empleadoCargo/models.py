from unicodedata import name
from django.db import models

# Create your models here
# 
# 
# Se crea una tabla para la base de datos.

class Empleado(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dni=models.IntegerField()

