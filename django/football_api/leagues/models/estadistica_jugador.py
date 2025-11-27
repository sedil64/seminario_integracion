from django.db import models

class EstadisticaJugador(models.Model):
    jugador = models.ForeignKey('Jugador', on_delete=models.CASCADE, related_name='estadisticas')
    partido = models.ForeignKey('Partido', on_delete=models.CASCADE, related_name='estadisticas')
    goles = models.IntegerField(default=0)
    asistencias = models.IntegerField(default=0)
    tarjetas_amarillas = models.IntegerField(default=0)
    tarjetas_rojas = models.IntegerField(default=0)
    minutos_jugados = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        unique_together = ('jugador', 'partido')

    def __str__(self):
        return f"{self.jugador} - {self.partido}"