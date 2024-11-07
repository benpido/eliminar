from django.db import models  # Importa el módulo de modelos de Django para definir modelos de base de datos.

# Define el modelo `Tabla1` que representa una tabla en la base de datos.
class Tabla1(models.Model):
    char_field = models.CharField(max_length=255)  # Campo de texto corto con un máximo de 255 caracteres.
    integer_field = models.IntegerField()  # Campo numérico que almacena enteros.
