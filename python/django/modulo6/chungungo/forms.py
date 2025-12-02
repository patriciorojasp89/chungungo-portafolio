from django import forms
from .models import Step


class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ["title", "description", "order", "is_completed"]
        labels = {
            "title": "Título",
            "description": "Descripción",
            "order": "Orden",
            "is_completed": "¿Completado?",
        }
