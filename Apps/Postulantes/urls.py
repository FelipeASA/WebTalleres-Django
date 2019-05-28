from django.urls import path, include

from Apps.Postulantes.views import *

urlpatterns = [
    path('', postulantes_listar, name="postulantes_listar"),
    path('crear/', postulantes_crear, name="postulantes_crear"),
    path('borrar/<int:id>/', postulantes_borrar, name="postulantes_borrar"),
]
