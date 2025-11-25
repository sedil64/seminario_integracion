from rest_framework import viewsets, filters
from leagues.models import Team
from leagues.serializers import TeamSerializer
from leagues.permissions import IsAdminOrReadOnly
from leagues.pagination import StandardResultsSetPagination

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.select_related('league').all()
    serializer_class = TeamSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name','slug','league__name','city')
    ordering_fields = ('name','founded_year')

    def get_queryset(self):
        qs = super().get_queryset()
        league_id = self.request.query_params.get('league')
        if league_id:
            qs = qs.filter(league__id=league_id)
        return qs
