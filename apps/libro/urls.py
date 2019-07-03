from django.urls import path
from .views import crearAutor, listarAutor

urlpatterns = [
    path('crear_autor/', crearAutor, name = 'crear_autor'),
    path('listar_autores/', listarAutor, name = 'listar_autores')
]
