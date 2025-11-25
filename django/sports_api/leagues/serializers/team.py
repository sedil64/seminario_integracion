from rest_framework import serializers
from leagues.models import Team, League

class TeamSerializer(serializers.ModelSerializer):
    league_name = serializers.ReadOnlyField(source='league.name')
    league_id = serializers.PrimaryKeyRelatedField(
        source='league', queryset=League.objects.all(), write_only=True
    )

    class Meta:
        model = Team
        fields = (
            'id','name','slug','city','stadium','founded_year',
            'league_id','league_name'
        )
        read_only_fields = ('id', 'league_name')
