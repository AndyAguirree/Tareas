from django.db import models
from django.utils.text import slugify


class Prioridad(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Prioridad'
        verbose_name_plural = 'Prioridades'
        ordering = ['orden', 'nombre']

    def __str__(self):
        return self.nombre


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)


class Tarea(models.Model):
    titulo = models.CharField(max_length=120, unique=True)
    descripcion = models.TextField(blank=True)
    prioridad = models.ForeignKey(Prioridad, on_delete=models.PROTECT, related_name='tareas')
    etiquetas = models.ManyToManyField(Etiqueta, blank=True, related_name='tareas')

    completada = models.BooleanField(default=False)
    creada = models.DateTimeField(auto_now_add=True)
    actualizada = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['completada', '-actualizada']

    def __str__(self):
        return self.titulo

