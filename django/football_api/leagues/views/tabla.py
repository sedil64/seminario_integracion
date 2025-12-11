from rest_framework import viewsets, filters
from leagues.models import TablaPosiciones
from leagues.serializers.tabla import TablaPosicionesSerializer
from leagues.permissions import IsAdminOrReadOnly
from leagues.pagination import StandardResultsSetPagination

class TablaPosicionesViewSet(viewsets.ModelViewSet):
    queryset = TablaPosiciones.objects.select_related('liga', 'equipo').all()
    serializer_class = TablaPosicionesSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('equipo__nombre', 'liga__nombre')
    ordering_fields = ('posicion', 'puntos', 'goles_favor')

    def get_queryset(self):
        qs = super().get_queryset()
        liga = self.request.query_params.get('liga')
        if liga:
            qs = qs.filter(liga__id=liga)
        return qs