from django import forms
from Apps.Talleres.models import *

class TallerCrearForm(forms.ModelForm):
    class Meta:
        model = TalleresModelo

        fields=[
            'nombre', 
            'detalle',
            'horas',
            'cupos',
        ]

        labels={
            'nombre':'Nombre',
            'detalle':'Detalle',
            'horas':'Horas',
            'cupos':'Cupos',
        }

        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'detalle':forms.TextInput(attrs={'class':'form-control'}),
            'horas':forms.NumberInput(attrs={'class':'form-control'}),
            'cupos':forms.NumberInput(attrs={'class':'form-control'}),
        }


