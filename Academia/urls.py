from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('/', admin.site.urls),
    path('talleres/', include('Apps.Talleres.urls')),
    path('postul/', include('Apps.Postulantes.urls')),
]
