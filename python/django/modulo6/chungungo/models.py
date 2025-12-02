from django.db import models


class Step(models.Model):
    title = models.CharField("Título", max_length=200)
    description = models.TextField("Descripción", blank=True)
    order = models.PositiveIntegerField("Orden", default=1)
    is_completed = models.BooleanField("Completado", default=False)

    created_at = models.DateTimeField("Creado el", auto_now_add=True)
    updated_at = models.DateTimeField("Actualizado el", auto_now=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Paso"
        verbose_name_plural = "Pasos"

    def __str__(self) -> str:
        return f"{self.order}. {self.title}"
