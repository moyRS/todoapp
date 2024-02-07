from django.shortcuts import render, redirect
from .models import Tarea
# Create your views here.

def index(request):
    tareas = Tarea.objects.all()
    if request.method == 'POST':
        nueva_tarea = Tarea(descripcion = request.POST['descripcion'])
        nueva_tarea.save()
        return redirect('index')
    return render(request, 'index.html', {'tareas': tareas})

def completar_tarea(request, tarea_id):
    tarea = Tarea.objects.get(pk = tarea_id)
    tarea.completada = True
    tarea.save()
    return redirect('index')


def eliminar_tarea(request, tarea_id):
    tarea = Tarea.objects.get(pk = tarea_id)
    tarea.delete()
    return redirect('index')

    








