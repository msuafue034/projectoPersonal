from django.shortcuts import render
from .models import Objetivo, ObjetivoUsuario, Registro, Nivel
#from .forms import ObjetivosForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, 'fitt/index.html')

##################* REGISTRO *#################
class RegistroView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('index') #? Luego va a ir a login (tiene más sentido), index es para probar


##################* OBJETIVOS *#################

class ObjetivoCreateView(LoginRequiredMixin, CreateView):
    model = Objetivo
    fields = ["descripcion"]
    template_name = "objetivos/create.html"
    success_url = reverse_lazy("objetivo_list")
    
class ObjetivoUpdateView(LoginRequiredMixin, UpdateView):
    model = Objetivo
    fields = ["descripcion"]
    template_name = "objetivos/update.html"
    success_url = reverse_lazy("objetivo_list")
    
class ObjetivoDeleteView(LoginRequiredMixin, DeleteView):
    model = Objetivo
    template_name = "objetivos/delete.html"
    success_url = reverse_lazy("objetivo_list")


##################* OBJETIVOS USUARIO *#################
class ObjetivoUsuarioListView(LoginRequiredMixin, ListView):
    model = ObjetivoUsuario
    template_name = "objetivosUsuario/list.html"
    context_object_name = "objetivosUsuario"

    def get_queryset(self):
        return ObjetivoUsuario.objects.filter(usuario=self.request.user)

class ObjetivoUsuarioCreateView(LoginRequiredMixin, CreateView):
    model = ObjetivoUsuario
    fields = ["objetivo", "tiempo"]
    template_name = "objetivosUsuario/create.html"
    success_url = reverse_lazy("objetivosUsuario_list")

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class ObjetivoUsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = ObjetivoUsuario
    fields = ["objetivo", "tiempo"]
    template_name = "objetivosUsuario/update.html"
    success_url = reverse_lazy("objetivosUsuario_list")

class ObjetivoUsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = ObjetivoUsuario
    template_name = "objetivosUsuario/delete.html"
    success_url = reverse_lazy("objetivosUsuario_list")


##################* ACTIVIDADES *#################
class RegistroListView(LoginRequiredMixin, ListView):
    model = Registro
    template_name = "registros/list.html"
    context_object_name = "registros"

    def get_queryset(self):
        return Registro.objects.filter(objetivo_usuario__usuario=self.request.user)

class RegistroCreateView(LoginRequiredMixin, CreateView):
    model = Registro
    fields = ["objetivo_usuario", "fecha", "duracion"]
    template_name = "registros/create.html"
    success_url = reverse_lazy("registro_list")

    def form_valid(self, form):
        if form.instance.objetivo_usuario.usuario != self.request.user:
            form.add_error(None, "No puedes agregar registros para otros usuarios.")
            return self.form_invalid(form)
        return super().form_valid(form)

class RegistroUpdateView(LoginRequiredMixin, UpdateView):
    model = Registro
    fields = ["fecha", "duracion"]
    template_name = "registros/update.html"
    success_url = reverse_lazy("registro_list")

class RegistroDeleteView(LoginRequiredMixin, DeleteView):
    model = Registro
    template_name = "registros/delete.html"
    success_url = reverse_lazy("registro_list")