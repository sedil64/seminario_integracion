from rest_framework import serializers
from leagues.models import Jugador, Equipo

class JugadorSerializer(serializers.ModelSerializer):
    equipo_nombre = serializers.ReadOnlyField(source='equipo.nombre')
    equipo_id = serializers.PrimaryKeyRelatedField(
        source='equipo', queryset=Equipo.objects.all(), write_only=True
    )

    class Meta:
        model = Jugador
        fields = (
            'id', 'nombre', 'apellido', 'fecha_nacimiento', 'nacionalidad',
            'posicion', 'numero_camiseta', 'altura_cm', 'foto_url',
            'equipo_id', 'equipo_nombre',
            'created_at', 'updated_at'
        )
        read_only_fields = ('id', 'created_at', 'updated_at', 'equipo_nombre')