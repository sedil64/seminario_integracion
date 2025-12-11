from rest_framework import viewsets, filters
from leagues.models import Liga
from leagues.serializers.liga import LigaSerializer
from leagues.permissions import IsAdminOrReadOnly

class LigaViewSet(viewsets.ModelViewSet):
    queryset = Liga.objects.all()
    serializer_class = LigaSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('nombre', 'pais', 'temporada')
    ordering_fields = ('nombre', 'pais', 'created_at')