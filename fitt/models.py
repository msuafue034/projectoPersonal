from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


##################! USUARIO !#################
class Usuario(AbstractUser):
    nombre = models.CharField(max_length=50, verbose_name="Nombre") 
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    email = models.EmailField(unique=True, verbose_name="Email")
    avatar = models.ImageField(upload_to="avatar/", blank=True, null=True, verbose_name="Foto de Perfil")
    fecha_registro = models.DateField(auto_now_add=True, verbose_name="Fecha de Registro")
    experiencia = models.PositiveIntegerField(default=0, verbose_name="Experiencia")
    nivel = models.PositiveIntegerField(default=1, verbose_name="Nivel")
    racha = models.PositiveIntegerField(default=0, verbose_name="Racha Actual")
    record = models.PositiveIntegerField(default=0, verbose_name="Racha Record")
    objetivos_marcados = models.BooleanField(default=False, verbose_name="Objetivos marcados")
 # UsuarioManager creado para controlar la creación de usuarios en terminal, ya que da errores al crear un superuser para poder entrar en /admin

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


##################! OBJETIVOS !#################
class Objetivo(models.Model):
    descripcion = models.CharField(max_length=100, verbose_name="Descripción")
    activado = models.BooleanField(default=False, verbose_name="Activado")

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Objetivo"
        verbose_name_plural = "Objetivos"

class ObjetivoUsuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario")
    objetivo = models.ForeignKey(Objetivo, on_delete=models.CASCADE, verbose_name="Objetivo")
    tiempo = models.PositiveIntegerField(verbose_name="Tiempo")
    
    def __str__(self):
        return f"{self.usuario.username} - {self.objetivo.descripcion}"

    class Meta:
        verbose_name = "Objetivo de Usuario"
        verbose_name_plural = "Objetivos de Usuario"


##################! ACTIVIDADES !#################
class RegistroActividad(models.Model):
    objetivoUsuario = models.ForeignKey(ObjetivoUsuario, on_delete=models.CASCADE, verbose_name="Objetivo Usuario")
    fecha = models.DateField(unique=True, verbose_name="Fecha")
    duracion = models.PositiveIntegerField(verbose_name="Duración (min)")

    def __str__(self):
        return f"{self.objetivoUsuario.usuario.username} - {self.fecha}"

    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"
        unique_together = ('objetivoUsuario', 'fecha')  # Puede repetirse un campo, pero no los dos iguales (se pueden registrar las mismas actividades en fechas diferentes o actividades diferentes en la misma fecha)
        

##################! NIVEL !#################
class Nivel(models.Model):
    nivel = models.PositiveIntegerField(primary_key=True, verbose_name="Nivel")
    max_puntos = models.PositiveIntegerField(verbose_name="Puntos Máximos")
    min_puntos = models.PositiveIntegerField(verbose_name="Puntos Mínimos")

    def __str__(self):
        return f"Nivel {self.nivel}"

    class Meta:
        verbose_name = "Nivel"
        verbose_name_plural = "Niveles"
