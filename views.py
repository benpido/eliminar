from django.shortcuts import render, redirect
from django.http import HttpResponse
#import datetime
from django.urls import path
from .models import Tabla1

# Create your views here.
def home(request):
    return render(request,"index.html")
def read(request):
    datos = Tabla1.objects.all()  # Obtener todos los registros de la tabla
    return render(request, "read.html", {'datos': datos})
def add(request):
    if request.method == 'POST':
        # Obtener los datos del cuerpo de la solicitud POST
        char_field = request.POST.get('char_field')
        integer_field = request.POST.get('integer_field')

        # Crear y guardar el nuevo registro
        Tabla1.objects.create(
            char_field=char_field,
            integer_field=int(integer_field),
        )
        # Redirigir a la vista 'read' después de guardar
        return redirect('read')
def mostrar_formulario(request):
    return render(request, 'add.html')

def edit(request, id):
    instance = Tabla1.objects.get(id=id)  # Obtén el objeto por ID
    if request.method == 'POST':
        # Si es POST, actualiza el objeto
        instance.char_field = request.POST.get('char_field')
        instance.integer_field = request.POST.get('integer_field')
        instance.save()  # Guarda los cambios
        return redirect('read')  # Redirige a la lista de datos
    # Si no es POST, muestra el formulario con los datos actuales
    return render(request, 'edit.html', {'instance': instance})