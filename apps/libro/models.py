from django.db import models

# Create your models here.

class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 255, blank = False, null = False)
    apellidos = models.CharField(max_length = 255, blank = False, null = False)
    nacionalidad = models.CharField(max_length = 50, blank = False, null = False)
    descripcion = models.TextField(blank = False, null = False)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nombre
