from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/registro/', RegistroView.as_view(), name="registroUsuario"), # Registro de usuario en la web
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
    
    path('perfil', views.perfil, name='perfil'),
    
    path('objetivos/create/', ObjetivoCreateView.as_view(), name='objetivo_create'),
    path('objetivos/<int:pk>/update/', ObjetivoUpdateView.as_view(), name='objetivo_update'),
    path('objetivos/<int:pk>/delete/', ObjetivoDeleteView.as_view(), name='objetivo_delete'),
    
    path('objetivos-usuario/', ObjetivoUsuarioListView.as_view(), name='objetivoUsuario'),
    path('objetivos-usuario/create/', ObjetivoUsuarioCreateView.as_view(), name='objetivoUsuario_create'),
    path('objetivos-usuario/<int:pk>/update/', ObjetivoUsuarioUpdateView.as_view(), name='objetivoUsuario_update'),
    path('objetivos-usuario/<int:pk>/delete/', ObjetivoUsuarioDeleteView.as_view(), name='objetivoUsuario_delete'),
    
    path('registros/<int:pk>/update/', RegistroUpdateView.as_view(), name='registro_update'),   # Registro de actividades (actualizar)
    path('registros/<int:pk>/delete/', RegistroDeleteView.as_view(), name='registro_delete'),   # Registro de actividades (eliminar)
]