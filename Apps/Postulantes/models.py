from django.db import models

from Apps.Talleres.models import TalleresModelo

# Create your models here.

class PostulantesModelo(models.Model):
    taller=models.ForeignKey(TalleresModelo, null=False, blank=False, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=100)
    email=models.EmailField()
    fono=models.IntegerField()

    def __str__(self):
        return self.nombre


