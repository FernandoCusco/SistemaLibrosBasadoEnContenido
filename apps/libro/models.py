from django.db import models

# Create your models here.

class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombres',max_length = 255, blank = False, null = False)
    apellidos = models.CharField('Apellidos', max_length = 255, blank = False, null = False)
    nacionalidad = models.CharField('Nacionalidad', max_length = 50, blank = False, null = False)
    descripcion = models.CharField('Descripcion', max_length = 50, blank = True, null = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
