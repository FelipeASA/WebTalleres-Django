from django import forms

from Apps.Postulantes.models import PostulantesModelo

class PostulantesForm(forms.ModelForm):
    class Meta:
        model = PostulantesModelo

        fields = ['nombre', 'email', 'fono', 'taller']

        label= {
            'nombre':'Nombre',
            'email':'Email',
            'fono':'Fono',
            'taller':'Taller'
         } # 1ra col campos, 2da Texto en el html

        widgets= {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'fono': forms.NumberInput(attrs={'class':'form-control'}),
            'taller': forms.Select(attrs={'class':'form-control'})
        }


