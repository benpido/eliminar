from django.db import models

# Create your models here.
class Tabla1(models.Model):
    char_field = models.CharField(max_length=255)  # Campo de texto
    integer_field = models.IntegerField()  # Campo numérico
