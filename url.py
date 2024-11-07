from django.urls import path
from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name = "home"),
    path("read/", views.read, name = "read"),
    path("agregar_datos/", views.add, name="agregar_datos"),
    path("mostrar_formulario/", views.mostrar_formulario, name="mostrar_formulario"),
    path("editar/<int:id>/", views.edit, name="editar_datos"),  # URL para editar datos
    ]