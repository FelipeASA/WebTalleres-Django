from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from Apps.Talleres.models import TalleresModelo
from Apps.Talleres.forms import TallerCrearForm

# Create your views here.

def talleres_listar(request):
    datos = TalleresModelo.objects.all()
    contexto = {'lista': datos}
    return render(request, 'talleres/talleres_listar.html', contexto)


def talleres_crear(request):
    if request.method == "POST":
        form = TallerCrearForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('talleres_listar')
    else:
        form=TallerCrearForm()

    contexto = {'form': form}
    return render(request, 'talleres/talleres_crear.html', contexto)



def talleres_eliminar(request, id):
    # obtenemos el modelo taller
    taller = TalleresModelo.objects.get(id = id)
    if request.method == "POST":
        taller.delete()
        return redirect('talleres_listar')
    else:
        return render(request, 'talleres/talleres_eliminar.html', {'taller': taller})



def talleres_editar(request, id):
    # otenemos el modelo taller
    taller = TalleresModelo.objects.get(id = id)
    if request.method == "GET":
        form=TallerCrearForm(instance=taller)
    else:
        form=TallerCrearForm(request.POST, instance=taller)
        if form.is_valid():
            form.save()
            return redirect('talleres_listar')
    contexto = {'form': form}
    return render(request, 'talleres/talleres_editar.html', contexto)


def talleres_json(request):
    datos = TalleresModelo.objects.all()
    qs_json = serializers.serialize('json', datos)
    return HttpResponse(qs_json, content_type='application/json')

