from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    ciudad = models.CharField(max_length=100, blank=True)
    estadio = models.CharField(max_length=100, blank=True)
    fundacion_anio = models.IntegerField(null=True, blank=True)
    entrenador = models.CharField(max_length=100, blank=True)
    escudo_url = models.URLField(max_length=255, blank=True)
    color_principal = models.CharField(max_length=30, blank=True)
    ligas = models.ManyToManyField('Liga', related_name='equipos', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("nombre",)

    def __str__(self):
        return self.nombre