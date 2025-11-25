from rest_framework import serializers
from matches.models import Match
from leagues.models import Team, League

class MatchSerializer(serializers.ModelSerializer):
    league_name = serializers.ReadOnlyField(source='league.name')
    home_team_name = serializers.ReadOnlyField(source='home_team.name')
    away_team_name = serializers.ReadOnlyField(source='away_team.name')

    league_id = serializers.PrimaryKeyRelatedField(
        source='league', queryset=League.objects.all(), write_only=True
    )
    home_team_id = serializers.PrimaryKeyRelatedField(
        source='home_team', queryset=Team.objects.all(), write_only=True
    )
    away_team_id = serializers.PrimaryKeyRelatedField(
        source='away_team', queryset=Team.objects.all(), write_only=True
    )

    class Meta:
        model = Match
        fields = (
            'id','league_id','league_name',
            'home_team_id','home_team_name',
            'away_team_id','away_team_name',
            'match_date','status',
            'home_score','away_score',
            'created_at',
        )
        read_only_fields = ('id','league_name','home_team_name','away_team_name','created_at')
