from django.shortcuts import render
from .models import Objetivo, ObjetivoUsuario, RegistroActividad, Nivel
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .forms import UsuarioCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='/accounts/login/')
def index(request): 
    return render(request, 'fitt/index.html')

##################* REGISTRO, LOGIN Y LOGOUT *#################

User = get_user_model()     # Para recoger el modelo de usuario definido, no el prederterminado

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['usuario', 'nombre', 'apellidos', 'email', 'password1', 'password2']
class RegistroView(CreateView):
    form_class = UsuarioCreationForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        usuario = form.cleaned_data.get("usuario")

        if User.objects.filter(usuario=usuario).exists():
            messages.error(self.request, "El nombre de usuario ya está en uso. Por favor, elige otro.")
            return render(self.request, self.template_name, {"form": form})          # Return al form CON ERROR

        return super().form_valid(form)
    
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    
    def form_valid(self, form):
        messages.success(self.request, 'Bienvenido de nuevo a F!tt :)')
        return super().form_valid(form)

class CustomLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'

    def get_next_page(self):
        return reverse_lazy('login')


    
##################* OBJETIVOS *#################

class ObjetivoCreateView(LoginRequiredMixin, CreateView):
    model = Objetivo
    fields = ["descripcion"]
    template_name = "objetivos_create.html"
    success_url = reverse_lazy("objetivo_list")
    
class ObjetivoUpdateView(LoginRequiredMixin, UpdateView):
    model = Objetivo
    fields = ["descripcion"]
    template_name = "objetivos_update.html"
    success_url = reverse_lazy("objetivo_list")
    
class ObjetivoDeleteView(LoginRequiredMixin, DeleteView):
    model = Objetivo
    template_name = "objetivos_delete.html"
    success_url = reverse_lazy("objetivo_list")


##################* OBJETIVOS USUARIO *#################
class ObjetivoUsuarioListView(LoginRequiredMixin, ListView):
    model = ObjetivoUsuario
    template_name = "objetivosUsuario_list.html"
    context_object_name = "objetivosUsuario"

    def get_queryset(self):
        return ObjetivoUsuario.objects.filter(usuario=self.request.user)

class ObjetivoUsuarioCreateView(LoginRequiredMixin, CreateView):
    model = ObjetivoUsuario
    fields = ["objetivo", "tiempo"]
    template_name = "objetivosUsuario_create.html"
    success_url = reverse_lazy("objetivosUsuario_list")

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class ObjetivoUsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = ObjetivoUsuario
    fields = ["objetivo", "tiempo"]
    template_name = "objetivosUsuario_update.html"
    success_url = reverse_lazy("objetivosUsuario_list")

class ObjetivoUsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = ObjetivoUsuario
    template_name = "objetivosUsuario_delete.html"
    success_url = reverse_lazy("objetivosUsuario_list")


##################* ACTIVIDADES *#################
class RegistroListView(LoginRequiredMixin, ListView):
    model = RegistroActividad
    template_name = "registros_list.html"
    context_object_name = "registros"

    def get_queryset(self):
        return RegistroActividad.objects.filter(objetivo_usuario__usuario=self.request.user)

class RegistroCreateView(LoginRequiredMixin, CreateView):
    model = RegistroActividad
    fields = ["objetivo_usuario", "fecha", "duracion"]
    template_name = "registros_create.html"
    success_url = reverse_lazy("registro_list")

    def form_valid(self, form):
        if form.instance.objetivo_usuario.usuario != self.request.user:
            form.add_error(None, "No puedes agregar registros para otros usuarios.")
            return self.form_invalid(form)
        return super().form_valid(form)

class RegistroUpdateView(LoginRequiredMixin, UpdateView):
    model = RegistroActividad
    fields = ["fecha", "duracion"]
    template_name = "registros_update.html"
    success_url = reverse_lazy("registro_list")

class RegistroDeleteView(LoginRequiredMixin, DeleteView):
    model = RegistroActividad
    template_name = "registros_delete.html"
    success_url = reverse_lazy("registro_list")