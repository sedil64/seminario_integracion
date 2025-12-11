from django.db import models

class TablaPosiciones(models.Model):
    liga = models.ForeignKey('Liga', on_delete=models.CASCADE, related_name='tabla_posiciones')
    equipo = models.ForeignKey('Equipo', on_delete=models.CASCADE, related_name='posiciones')
    posicion = models.IntegerField()
    partidos_jugados = models.IntegerField(default=0)
    ganados = models.IntegerField(default=0)
    empatados = models.IntegerField(default=0)
    perdidos = models.IntegerField(default=0)
    goles_favor = models.IntegerField(default=0)
    goles_contra = models.IntegerField(default=0)
    puntos = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("posicion",)
        unique_together = ('liga', 'equipo')

    def __str__(self):
        return f"{self.equipo} - Pos {self.posicion}"