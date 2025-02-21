from django import forms
from .models import Usuario, Objetivo, ObjetivoUsuario, RegistroActividad
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

class RegistroUsuarioForm(forms.ModelForm):
    duracion = forms.IntegerField(min_value=0, max_value=1440, required=True)

    class Meta:
        model = RegistroActividad
        fields = ['objetivoUsuario', 'fecha', 'duracion']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def save(self, commit=True):
        
        newRegistro = super().save(commit=False)
        newRegistro.objetivoUsuario = self.cleaned_data['objetivoUsuario']
        newRegistro.duracion = self.cleaned_data['duracion']
        
        if commit:
            newRegistro.save()
            
        return newRegistro





        
