from django.shortcuts import render, redirect
from .forms import AutorForm
from .models import Autor

# Create your views here.
def Home(request):
    return render(request, 'index.html')


def crearAutor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        print(autor_form)

        if autor_form.is_valid():
            autor_form.save()
            return redirect('index')

    else:
        autor_form = AutorForm()
        print(autor_form)
    return render(request, 'libro/crear_autor.html', {'autor_form':autor_form})

def listarAutor(request):
    autores = Autor.objects.all()
    return render(request, 'libro/listar_autores.html', {'autores':autores})
