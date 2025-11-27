from rest_framework import serializers
from leagues.models import EstadisticaJugador, Jugador, Partido

class EstadisticaJugadorSerializer(serializers.ModelSerializer):
    jugador_nombre = serializers.SerializerMethodField(read_only=True)
    partido_resumen = serializers.SerializerMethodField(read_only=True)
    
    jugador_id = serializers.PrimaryKeyRelatedField(
        source='jugador', queryset=Jugador.objects.all(), write_only=True
    )
    partido_id = serializers.PrimaryKeyRelatedField(
        source='partido', queryset=Partido.objects.all(), write_only=True
    )

    class Meta:
        model = EstadisticaJugador
        fields = (
            'id', 'jugador_id', 'jugador_nombre',
            'partido_id', 'partido_resumen',
            'goles', 'asistencias', 'tarjetas_amarillas', 
            'tarjetas_rojas', 'minutos_jugados',
            'created_at', 'updated_at'
        )
        read_only_fields = ('id', 'created_at', 'updated_at', 
                           'jugador_nombre', 'partido_resumen')

    def get_jugador_nombre(self, obj):
        return f"{obj.jugador.nombre} {obj.jugador.apellido}"

    def get_partido_resumen(self, obj):
        return f"{obj.partido.equipo_local.nombre} vs {obj.partido.equipo_visitante.nombre}"