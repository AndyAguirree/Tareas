from django.contrib import admin

from .models import Prioridad, Etiqueta, Tarea

admin.site.register(Prioridad)
admin.site.register(Etiqueta)
admin.site.register(Tarea)

