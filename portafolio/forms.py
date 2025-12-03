from django import forms
from .models import Proyecto


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = [
            "titulo",
            "descripcion",
            "url_demo",
            "url_codigo",
            "fecha_creacion",
            "esta_activo",
            "skills",  
        ]
