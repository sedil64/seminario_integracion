from django.db import models
from django.core.exceptions import ValidationError

class Partido(models.Model):
    ESTADOS = [
        ('Programado', 'Programado'),
        ('En Vivo', 'En Vivo'),
        ('Finalizado', 'Finalizado'),
        ('Suspendido', 'Suspendido'),
    ]
    
    liga = models.ForeignKey('Liga', on_delete=models.CASCADE, related_name='partidos')
    equipo_local = models.ForeignKey('Equipo', on_delete=models.CASCADE, related_name='partidos_local')
    equipo_visitante = models.ForeignKey('Equipo', on_delete=models.CASCADE, related_name='partidos_visitante')
    fecha_hora = models.DateTimeField()
    jornada = models.IntegerField(null=True, blank=True)
    goles_local = models.IntegerField(default=0)
    goles_visitante = models.IntegerField(default=0)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Programado')
    estadio = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-fecha_hora",)

    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante}"