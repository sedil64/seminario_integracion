from django.db import models

class Jugador(models.Model):
    POSICIONES = [
        ('Portero', 'Portero'),
        ('Defensa', 'Defensa'),
        ('Mediocampista', 'Mediocampista'),
        ('Delantero', 'Delantero'),
    ]
    
    equipo = models.ForeignKey('Equipo', on_delete=models.CASCADE, related_name='jugadores')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    nacionalidad = models.CharField(max_length=50, blank=True)
    posicion = models.CharField(max_length=30, choices=POSICIONES)
    numero_camiseta = models.IntegerField(null=True, blank=True)
    altura_cm = models.IntegerField(null=True, blank=True)
    foto_url = models.URLField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("apellido", "nombre")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"