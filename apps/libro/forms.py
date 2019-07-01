from django import forms
from .models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor                                                   #definimos el modelo
        fields = ['nombre', 'apellidos', 'nacionalidad', 'descripcion'] #campos para interactuar, dentro de una lista
