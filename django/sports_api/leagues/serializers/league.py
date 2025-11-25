from rest_framework import serializers
from leagues.models import League

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ('id', 'name', 'slug', 'country', 'created_at')
        read_only_fields = ('id', 'created_at')
