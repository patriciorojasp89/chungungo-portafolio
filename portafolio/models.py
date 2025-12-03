from django.db import models


class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    url_demo = models.URLField(blank=True)
    url_codigo = models.URLField(blank=True)
    fecha_creacion = models.DateField(null=True, blank=True)
    esta_activo = models.BooleanField(default=True)
    skills = models.ManyToManyField("Skill", blank=True, related_name="proyectos")
    def __str__(self):
        return self.titulo


class Skill(models.Model):
    nombre = models.CharField(max_length=50)
    nivel = models.CharField(
        max_length=20,
        choices=[
            ("basico", "Básico"),
            ("intermedio", "Intermedio"),
            ("avanzado", "Avanzado"),
        ],
        default="intermedio",
    )

    def __str__(self):
        return f"{self.nombre} ({self.nivel})"


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    mensaje = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.correo}"

class PerfilUsuario(models.Model):
    contacto = models.OneToOneField(
        Contacto, on_delete=models.CASCADE, related_name="perfil"
    )
    telefono = models.CharField(max_length=20, blank=True)
    ciudad = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"Perfil de {self.contacto.nombre}"


class TareaProyecto(models.Model):
    proyecto = models.ForeignKey(
        Proyecto, on_delete=models.CASCADE, related_name="tareas"
    )
    titulo = models.CharField(max_length=100)
    completada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.titulo} ({'ok' if self.completada else 'pendiente'})"


