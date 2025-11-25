from rest_framework import viewsets, filters
from leagues.models import League
from leagues.serializers import LeagueSerializer
from leagues.permissions import IsAdminOrReadOnly

class LeagueViewSet(viewsets.ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name','country','slug')
    ordering_fields = ('name','created_at')
