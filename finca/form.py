from django import forms
from .models import Propiedad, Datos

class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = '__all__'

class DatosForm(forms.ModelForm):
    class Meta:
        model = Datos
        fields = '__all__'