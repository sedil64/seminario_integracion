from rest_framework import viewsets, filters
from leagues.models import EstadisticaJugador
from leagues.serializers.estadistica import EstadisticaJugadorSerializer
from leagues.permissions import IsAdminOrReadOnly
from leagues.pagination import StandardResultsSetPagination

class EstadisticaJugadorViewSet(viewsets.ModelViewSet):
    queryset = EstadisticaJugador.objects.select_related('jugador', 'partido').all()
    serializer_class = EstadisticaJugadorSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('jugador__nombre', 'jugador__apellido')
    ordering_fields = ('goles', 'asistencias', 'created_at')

    def get_queryset(self):
        qs = super().get_queryset()
        jugador = self.request.query_params.get('jugador')
        partido = self.request.query_params.get('partido')
        if jugador:
            qs = qs.filter(jugador__id=jugador)
        if partido:
            qs = qs.filter(partido__id=partido)
        return qs