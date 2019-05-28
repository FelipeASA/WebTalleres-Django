from django.shortcuts import render, redirect
from django.http import HttpResponse

from Apps.Postulantes.forms import PostulantesForm
from Apps.Postulantes.models import PostulantesModelo

# Create your views here.

def postulantes_listar(request):
    datos = PostulantesModelo.objects.all()
    contexto = {'lista': datos}
    return render(request, 'postul/postulantes_listar.html', contexto)

def postulantes_crear(request):
    if request.method == 'POST':
        form = PostulantesForm(request.POST) # definimos variable tipo formulario
        if form.is_valid():
            form.save()
        return redirect('postulantes_listar')
    else:
        form=PostulantesForm()
    return render(request, "postul/postulantes_crear.html", {'postulacion':form})

def postulantes_borrar(request, id):
    postulante = PostulantesModelo.objects.get(id=id)
    if request.method == "POST":
        postulante.delete()
        return redirect('postulantes_listar')
    else:
        return render(request, 'postul/postulantes_borrar.html', {'p': postulante})

