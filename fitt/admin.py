from django.contrib import admin
from .models import Usuario, Objetivo, ObjetivoUsuario, RegistroActividad, Nivel

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'nombre', 'apellidos', 'email', 'nivel', 'racha', 'record', 'fecha_registro')  #! Revisar por posible modificación en models
    search_fields = ('username', 'email', 'nombre', 'apellidos')
    list_filter = ('nivel', 'fecha_registro')
    ordering = ('fecha_registro',)

@admin.register(Objetivo)
class ObjetivoAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)
    search_fields = ('descripcion',)

@admin.register(ObjetivoUsuario)
class ObjetivoUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'objetivo', 'tiempo')
    search_fields = ('usuario__usuario', 'objetivo__descripcion')
    list_filter = ('usuario',)

@admin.register(RegistroActividad)
class RegistroActividadAdmin(admin.ModelAdmin):
    list_display = ('objetivoUsuario', 'fecha', 'duracion')
    search_fields = ('objetivoUsuario__usuario__usuario', 'fecha')
    list_filter = ('fecha',)
    ordering = ('fecha',)

@admin.register(Nivel)
class NivelAdmin(admin.ModelAdmin):
    list_display = ('nivel', 'max_puntos', 'min_puntos')
    ordering = ('nivel',)
