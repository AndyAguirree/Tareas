from django import forms

from .models import Tarea


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'prioridad', 'etiquetas', 'completada']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
            'etiquetas': forms.CheckboxSelectMultiple(),
        }

