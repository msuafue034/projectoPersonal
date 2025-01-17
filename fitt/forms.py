from django import forms
from .models import Usuario, Objetivo, ObjetivoUsuario
from datetime import date

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['usuario', 'nombre', 'apellidos', 'email']

class ObjetivoForm(forms.ModelForm):
    class Meta:
        model = Objetivo
        fields = '__all__'
        
class ObjetivoUsuarioForm(forms.ModelForm):
    
    class Meta:
        model = ObjetivoUsuario
        fields = '__all__'
        
