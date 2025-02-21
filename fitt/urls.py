from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('accounts/registro/', RegistroView.as_view(), name="registro"), # Registro de usuario en la web
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
    
    path('perfil/', PerfilView.as_view(), name='perfil'),
    path('perfil/<int:pk>/update/', PerfilUpdateView.as_view(), name='perfil_update'),
    
    path('seguimiento/', SeguimientoView.as_view(), name='seguimiento'),
    path('logros/', LogrosView.as_view(), name='logros'),
    
    path('objetivos/create/', ObjetivoUsuarioCreateView.as_view(), name='objetivo_create'),
    path('objetivos/<int:pk>/delete/', ObjetivoUsuarioDeleteView.as_view(), name='objetivo_delete'),
    
    path('registro/create/', RegistroCreateView.as_view(), name='registro_create'),
    path('registros/<int:pk>/update/', RegistroUpdateView.as_view(), name='registro_update'),   # Registro de actividades (actualizar)
    path('registros/<int:pk>/delete/', RegistroDeleteView.as_view(), name='registro_delete'),   # Registro de actividades (eliminar)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)