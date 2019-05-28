from django.urls import path, include

from Apps.Talleres.views import *

# importamos de la app ventas

urlpatterns = [
    path('', talleres_listar, name='talleres_listar'),
    path('crear/', talleres_crear, name='talleres_crear'),
    path('eliminar/<int:id>/', talleres_eliminar, name='talleres_eliminar'),
    path('editar/<int:id>/', talleres_editar, name='talleres_editar'),
]
