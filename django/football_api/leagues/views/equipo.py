from rest_framework import viewsets, filters
from leagues.models import Equipo
from leagues.serializers.equipo import EquipoSerializer
from leagues.permissions import IsAdminOrReadOnly
from leagues.pagination import StandardResultsSetPagination

class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.prefetch_related('ligas').all()
    serializer_class = EquipoSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('nombre', 'ciudad', 'entrenador')
    ordering_fields = ('nombre', 'ciudad', 'created_at')