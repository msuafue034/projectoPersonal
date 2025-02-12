from django import forms
from .models import Usuario, Objetivo, ObjetivoUsuario
from django.contrib.auth.forms import UserCreationForm

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'nombre', 'apellidos', 'email', 'password1', 'password2']
        
class ObjetivoForm(forms.ModelForm):
    class Meta:
        model = Objetivo
        fields = '__all__'
        
class ObjetivoUsuarioForm(forms.ModelForm):
    
    class Meta:
        model = ObjetivoUsuario
        fields = '__all__'
        
