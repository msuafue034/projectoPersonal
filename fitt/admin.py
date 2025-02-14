from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Usuario, Objetivo, ObjetivoUsuario, RegistroActividad, Nivel

# Register your models here.

# @admin.register(Usuario)
# class UsuarioAdmin(admin.ModelAdmin):   
    
#     list_display = ('username', 'nombre', 'apellidos', 'email', 'nivel', 'racha', 'record', 'fecha_registro', 'mostrar_objetivos')  #! Revisar por posible modificación en models
#     search_fields = ('username', 'email', 'nombre', 'apellidos')
#     list_filter = ('nivel', 'fecha_registro')
#     ordering = ('fecha_registro',)

# Register your models here.
class ObjetivoUsuarioInline(admin.TabularInline):  # También puedes usar StackedInline
    model = ObjetivoUsuario
    extra = 1
class CustomUserAdmin(UserAdmin):
    model = Usuario
    
     # Agregar los nuevos campos a fieldsets (para edición de usuario)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('nombre', 'apellidos', 'nivel', 'racha', 'record')}),  # Agrega solo los nuevos campos
    )
    inlines = [ObjetivoUsuarioInline] 

    # Agregar los nuevos campos a add_fieldsets (para crear usuario)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('nombre', 'apellidos', 'nivel', 'racha', 'record')}),
    )
    
admin.site.register(Usuario, CustomUserAdmin)    

@admin.register(Objetivo)
class ObjetivoAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)
    search_fields = ('descripcion',)

@admin.register(ObjetivoUsuario)
class ObjetivoUsuarioAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'objetivo', 'tiempo')
    search_fields = ('usuario__username', 'objetivo__descripcion')
    list_filter = ('usuario',)

    def get_username(self, obj):
        return obj.usuario.username
    get_username.short_description = "Usuario"
    
@admin.register(RegistroActividad)
class RegistroActividadAdmin(admin.ModelAdmin):
    list_display = ('objetivoUsuario', 'fecha', 'duracion')
    search_fields = ('objetivoUsuario__usuario__username', 'fecha')
    list_filter = ('fecha',)
    ordering = ('fecha',)
    
    def get_username(self, obj):
        return obj.objetivoUsuario.usuario.username
    get_username.short_description = "Usuario"

@admin.register(Nivel)
class NivelAdmin(admin.ModelAdmin):
    list_display = ('nivel', 'max_puntos', 'min_puntos')
    ordering = ('nivel',)
