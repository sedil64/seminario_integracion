from rest_framework import serializers
from leagues.models import Equipo, Liga

class EquipoSerializer(serializers.ModelSerializer):
    ligas_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Liga.objects.all(), source='ligas', write_only=True, required=False
    )
    ligas_nombres = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Equipo
        fields = (
            'id', 'nombre', 'ciudad', 'estadio', 'fundacion_anio',
            'entrenador', 'escudo_url', 'color_principal',
            'ligas_ids', 'ligas_nombres',
            'created_at', 'updated_at'
        )
        read_only_fields = ('id', 'created_at', 'updated_at', 'ligas_nombres')

    def get_ligas_nombres(self, obj):
        return [f"{liga.nombre} ({liga.temporada})" for liga in obj.ligas.all()]