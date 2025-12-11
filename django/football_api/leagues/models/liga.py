from django.db import models

class Liga(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    temporada = models.CharField(max_length=20)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    logo_url = models.URLField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.nombre} - {self.temporada}"