from rest_framework import serializers
from leagues.models import Liga

class LigaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liga
        fields = (
            'id', 'nombre', 'pais', 'temporada', 
            'fecha_inicio', 'fecha_fin', 'logo_url',
            'created_at', 'updated_at'
        )
        read_only_fields = ('id', 'created_at', 'updated_at')