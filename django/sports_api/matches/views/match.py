from rest_framework import viewsets, filters, permissions
from matches.models import Match
from matches.serializers import MatchSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.select_related('league','home_team','away_team').all()
    serializer_class = MatchSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = (
        'league__name',
        'home_team__name',
        'away_team__name',
    )
    ordering_fields = ('match_date', 'created_at')

    def get_queryset(self):
        qs = super().get_queryset()
        league_id = self.request.query_params.get('league')
        team_id = self.request.query_params.get('team')
        status = self.request.query_params.get('status')

        if league_id:
            qs = qs.filter(league__id=league_id)
        if team_id:
            qs = qs.filter(home_team__id=team_id) | qs.filter(away_team__id=team_id)
        if status:
            qs = qs.filter(status=status)
        return qs
