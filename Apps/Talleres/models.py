from django.db import models

# Create your models here.

class TalleresModelo(models.Model):
    nombre=models.CharField(max_length=100)
    detalle=models.CharField(max_length=500)
    horas=models.IntegerField()
    cupos=models.IntegerField()

    def __str__(self):
        return self.nombre
