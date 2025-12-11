from rest_framework import serializers
from leagues.models import TablaPosiciones, Liga, Equipo

class TablaPosicionesSerializer(serializers.ModelSerializer):
    liga_nombre = serializers.ReadOnlyField(source='liga.nombre')
    equipo_nombre = serializers.ReadOnlyField(source='equipo.nombre')
    diferencia_goles = serializers.SerializerMethodField(read_only=True)
    
    liga_id = serializers.PrimaryKeyRelatedField(
        source='liga', queryset=Liga.objects.all(), write_only=True
    )
    equipo_id = serializers.PrimaryKeyRelatedField(
        source='equipo', queryset=Equipo.objects.all(), write_only=True
    )

    class Meta:
        model = TablaPosiciones
        fields = (
            'id', 'liga_id', 'liga_nombre', 'equipo_id', 'equipo_nombre',
            'posicion', 'partidos_jugados', 'ganados', 'empatados', 'perdidos',
            'goles_favor', 'goles_contra', 'diferencia_goles', 'puntos',
            'created_at', 'updated_at'
        )
        read_only_fields = ('id', 'created_at', 'updated_at', 
                           'liga_nombre', 'equipo_nombre', 'diferencia_goles')

    def get_diferencia_goles(self, obj):
        return obj.goles_favor - obj.goles_contra