from django.shortcuts import redirect, render
from .models import Usuario, Objetivo, ObjetivoUsuario, RegistroActividad, Nivel
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, View
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .forms import RegistroUsuarioForm, UsuarioCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import JsonResponse
# from django.contrib.auth.decorators import login_required

##################! INDEX !#################

# @login_required(login_url='/accounts/login/')
# def index(request): 
#     usuario = request.user
#     print(usuario.avatar)
#     return render(request, 'fitt/index.html', {'usuario': usuario})

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'fitt/index.html'
    login_url = '/accounts/login/'

    def get_context_data(self, **otros):
        contexto = super().get_context_data(**otros)
        usuario = self.request.user
        contexto['usuario'] = usuario
        contexto['objetivos_usuario'] = ObjetivoUsuario.objects.filter(usuario=usuario).select_related("objetivo")
        return contexto
    

##################! REGISTRO, LOGIN Y LOGOUT !#################

User = get_user_model()     # Para recoger el modelo de usuario definido, no el prederterminado

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'nombre', 'apellidos', 'email', 'password1', 'password2']
class RegistroView(CreateView):
    form_class = UsuarioCreationForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        usuario = form.cleaned_data.get("username")

        if User.objects.filter(username=usuario).exists():
            messages.error(self.request, "El nombre de usuario ya está en uso. Por favor, elige otro.")
            return render(self.request, self.template_name, {"form": form})          # Return al form CON ERROR

        return super().form_valid(form)

    #? AÑADIR OBJETIVOS MARCADOS EN UN FORM AL REGISTRO O PERMITIR VALOR POR DEFECTO
    
    
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    
    def form_valid(self, form):
        messages.success(self.request, 'Bienvenido de nuevo a F!tt :)')
        return super().form_valid(form)

class CustomLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'

    def get_next_page(self):
        return reverse_lazy('login')


##################! PERFIL !#################

# @login_required(login_url='/accounts/login/')
# def perfil(request):
#     usuario = request.user
#     print(usuario.avatar)
#     return render(request, 'fitt/perfil/perfil.html', {'usuario': usuario})

class PerfilView(LoginRequiredMixin, TemplateView):
    template_name = 'fitt/perfil/perfil.html'
    login_url = '/accounts/login/'

    def get_context_data(self, **otros):
        contexto = super().get_context_data(**otros)
        contexto['usuario'] = self.request.user
        print(self.request.user.avatar)
        return contexto


class PerfilUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    fields = ['nombre', 'apellidos', 'email']
    template_name = "fitt/perfil/perfil_update.html"
    success_url = reverse_lazy('perfil')
    
    def get_object(self, queryset=None):
        return self.request.user



##################! SEGUIMIENTO !#################
class SeguimientoView(LoginRequiredMixin, TemplateView):
    template_name = 'fitt/seguimiento/seguimiento.html'
    login_url = '/accounts/login/'

    def get_context_data(self, **otros):
        contexto = super().get_context_data(**otros)
        contexto['usuario'] = self.request.user
        print(self.request.user.avatar)
        return contexto


##################! LOGROS !#################
class LogrosView(LoginRequiredMixin, TemplateView):
    template_name = 'fitt/logros/logros.html'
    login_url = '/accounts/login/'

    def get_context_data(self, **otros):
        contexto = super().get_context_data(**otros)
        contexto['usuario'] = self.request.user
        print(self.request.user.avatar)
        return contexto
    
    
##################! OBJETIVOS !#################

class ObjetivoCreateView(LoginRequiredMixin, CreateView):
    model = Objetivo
    fields = ['descripcion']
    template_name = "fitt/objetivos/objetivos_create.html"
    success_url = reverse_lazy('objetivo_list')
    
class ObjetivoUpdateView(LoginRequiredMixin, UpdateView):
    model = Objetivo
    fields = ['descripcion']
    template_name = "fitt/objetivos/objetivos_update.html"
    success_url = reverse_lazy('objetivo_list')
    
class ObjetivoDeleteView(LoginRequiredMixin, DeleteView):
    model = Objetivo
    template_name = "fitt/objetivos/objetivos_delete.html"
    success_url = reverse_lazy('objetivo_list')

    

##################! OBJETIVOS USUARIO !#################
class ObjetivoUsuarioListView(LoginRequiredMixin, ListView):
    model = ObjetivoUsuario
    template_name = "objetivosUsuario_list.html"
    context_object_name = 'objetivosUsuario'

    def get_queryset(self):
        return ObjetivoUsuario.objects.filter(usuario=self.request.user)

class ObjetivoUsuarioCreateView(LoginRequiredMixin, CreateView):
    model = ObjetivoUsuario
    fields = ['objetivo']
    template_name = "fitt/objetivos/objetivos_create.html"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **otros):
        contexto = super().get_context_data(**otros)
        contexto['usuario'] = self.request.user
        print(self.request.user.avatar)
        
        # FILTRO PARA MOSTRAR SOLO LOS OBJETIVOS DISPONIBLES EN EL FORMULARIO
        asignados = ObjetivoUsuario.objects.filter(usuario = self.request.user).values_list('objetivo', flat=True)  # flat=True --> devuelve una lista de valores en lugar de una lista de tuplas para simplificar los resultados
        disponibles = Objetivo.objects.exclude(id__in = asignados)

        contexto['objetivos'] = disponibles
        return contexto


class ObjetivoUsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = ObjetivoUsuario
    template_name = "fitt/objetivos/objetivos_delete.html"
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **otros):
        contexto = super().get_context_data(**otros)
        contexto['usuario'] = self.request.user
        print(self.request.user.avatar)
        return contexto


##################! ACTIVIDADES !#################
class RegistroListView(LoginRequiredMixin, ListView):
    model = RegistroActividad
    template_name = "registros_list.html"
    context_object_name = "registros"

    def get_queryset(self):
        return RegistroActividad.objects.filter(objetivo_usuario__usuario=self.request.user)

class RegistroCreateView(LoginRequiredMixin, View):
    model = RegistroActividad
    fields = ["objetivoUsuario", "fecha", "duracion"]
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
  
        form = RegistroUsuarioForm(request.POST)
        
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "El registro se ha creado correctamente."}, status=201)
        return JsonResponse({"error": "Hubo un error al crear el registro. Inténtalo de nuevo."}, status=400)

class RegistroUpdateView(LoginRequiredMixin, UpdateView):
    model = RegistroActividad
    fields = ["fecha", "duracion"]
    template_name = "registros_update.html"
    success_url = reverse_lazy("index")

class RegistroDeleteView(LoginRequiredMixin, DeleteView):
    model = RegistroActividad
    template_name = "registros_delete.html"
    success_url = reverse_lazy("index")