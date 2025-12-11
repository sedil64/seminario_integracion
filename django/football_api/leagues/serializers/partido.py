from rest_framework import serializers
from leagues.models import Partido, Liga, Equipo

class PartidoSerializer(serializers.ModelSerializer):
    liga_nombre = serializers.ReadOnlyField(source='liga.nombre')
    equipo_local_nombre = serializers.ReadOnlyField(source='equipo_local.nombre')
    equipo_visitante_nombre = serializers.ReadOnlyField(source='equipo_visitante.nombre')
    
    liga_id = serializers.PrimaryKeyRelatedField(
        source='liga', queryset=Liga.objects.all(), write_only=True
    )
    equipo_local_id = serializers.PrimaryKeyRelatedField(
        source='equipo_local', queryset=Equipo.objects.all(), write_only=True
    )
    equipo_visitante_id = serializers.PrimaryKeyRelatedField(
        source='equipo_visitante', queryset=Equipo.objects.all(), write_only=True
    )

    class Meta:
        model = Partido
        fields = (
            'id', 'liga_id', 'liga_nombre',
            'equipo_local_id', 'equipo_local_nombre',
            'equipo_visitante_id', 'equipo_visitante_nombre',
            'fecha_hora', 'jornada', 'goles_local', 'goles_visitante',
            'estado', 'estadio',
            'created_at', 'updated_at'
        )
        read_only_fields = ('id', 'created_at', 'updated_at', 
                           'liga_nombre', 'equipo_local_nombre', 'equipo_visitante_nombre')

    def validate(self, data):
        return data