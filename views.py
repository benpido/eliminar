from django.shortcuts import render, redirect  # Importa funciones para renderizar plantillas y redirigir a otras URLs.
from django.http import HttpResponse  # Importa una clase para crear respuestas HTTP directamente (aunque no se utiliza en este archivo).
#import datetime  # Comentado: esta línea intenta importar el módulo datetime pero actualmente no se usa.
from django.urls import path  # Permite definir rutas, aunque aquí no se necesita ya que las rutas están en `urls.py`.
from .models import Tabla1  # Importa el modelo `Tabla1` desde `models.py` para interactuar con la base de datos.

# Define la vista principal de la aplicación.
def home(request):
    return render(request,"index.html")  # Renderiza y muestra el template `index.html` como página de inicio.

# Define la vista que muestra todos los datos de `Tabla1`.
def read(request):
    datos = Tabla1.objects.all()  # Obtiene todos los registros de la tabla `Tabla1`.
    return render(request, "read.html", {'datos': datos})  # Renderiza el template `read.html` pasando los datos.

# Define la vista que maneja la adición de datos.
def add(request):
    if request.method == 'POST':  # Verifica si la solicitud es POST.
        # Obtiene los valores de los campos enviados por el formulario.
        char_field = request.POST.get('char_field')
        integer_field = request.POST.get('integer_field')

        # Crea un nuevo registro en la tabla `Tabla1` con los datos obtenidos.
        Tabla1.objects.create(
            char_field=char_field,
            integer_field=int(integer_field),
        )
        # Redirige a la vista `read` después de guardar los datos.
        return redirect('read')

# Muestra el formulario para agregar datos.
def mostrar_formulario(request):
    return render(request, 'add.html')  # Renderiza el template `add.html`.

# Define la vista para editar datos existentes.
def edit(request, id):
    instance = Tabla1.objects.get(id=id)  # Obtiene un objeto específico de `Tabla1` según el `id` pasado.
    if request.method == 'POST':  # Si la solicitud es POST, procede a actualizar el objeto.
        instance.char_field = request.POST.get('char_field')  # Actualiza el campo `char_field`.
        instance.integer_field = request.POST.get('integer_field')  # Actualiza el campo `integer_field`.
        instance.save()  # Guarda los cambios en la base de datos.
        return redirect('read')  # Redirige a la vista de lista después de guardar los cambios.
    # Si no es POST, muestra el formulario de edición con los datos actuales del registro.
    return render(request, 'edit.html', {'instance': instance})
