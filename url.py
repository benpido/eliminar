from django.urls import path  # Importa la función `path` para definir rutas.
from . import views  # Importa el módulo `views` para enlazar las vistas con las URLs.

# Define las rutas de la aplicación.
urlpatterns = [
    path("", views.home, name="home"),  # Ruta de la página principal, enlaza con la vista `home`.
    path("read/", views.read, name="read"),  # Ruta para ver los datos en `Tabla1`, enlaza con la vista `read`.
    path("agregar_datos/", views.add, name="agregar_datos"),  # Ruta para agregar datos, enlaza con la vista `add`.
    path("mostrar_formulario/", views.mostrar_formulario, name="mostrar_formulario"),  # Ruta que muestra el formulario de adición de datos, enlaza con `mostrar_formulario`.
    path("editar/<int:id>/", views.edit, name="editar_datos"),  # Ruta para editar un registro específico, enlaza con `edit`.
]
