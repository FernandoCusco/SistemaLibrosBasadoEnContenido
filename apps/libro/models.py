from django.db import models

# Create your models here.

class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombres',max_length = 255, blank = False, null = False)
    apellidos = models.CharField('Apellidos', max_length = 255, blank = False, null = False)
    nacionalidad = models.CharField('Nacionalidad', max_length = 50, blank = False, null = False)
    descripcion = models.TextField('Descripcion',blank = False, null = False)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now = True, auto_now_add = False)


    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

    def __str__(self):   #nombre del campo no como Object
        return self.nombre


class Libro(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo', max_length = 255, blank = False, null = False)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now = True, auto_now_add = False)
    fecha_publicacion = models.DateField('Fecha de publicacion', blank = False, null = False)
    #autor_id = models.ForeignKey(Autor, on_delete=models.CASCADE) #relacion uno a muchos
    #autor_id = models.OneToOneField(Autor, on_delete=models.CASCADE) #relacion uno a uno
    autor_id = models.ManyToManyField(Autor) #relacion muchos a muchos

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str__(self):      #nombre del campo no como Object
        return self.titulo
