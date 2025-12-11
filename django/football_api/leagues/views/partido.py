from rest_framework import viewsets, filters
from leagues.models import Partido
from leagues.serializers.partido import PartidoSerializer
from leagues.permissions import IsAdminOrReadOnly
from leagues.pagination import StandardResultsSetPagination

class PartidoViewSet(viewsets.ModelViewSet):
    queryset = Partido.objects.select_related('liga', 'equipo_local', 'equipo_visitante').all()
    serializer_class = PartidoSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('equipo_local__nombre', 'equipo_visitante__nombre', 'estadio')
    ordering_fields = ('fecha_hora', 'jornada', 'created_at')

    def get_queryset(self):
        qs = super().get_queryset()
        liga = self.request.query_params.get('liga')
        estado = self.request.query_params.get('estado')
        jornada = self.request.query_params.get('jornada')
        if liga:
            qs = qs.filter(liga__id=liga)
        if estado:
            qs = qs.filter(estado=estado)
        if jornada:
            qs = qs.filter(jornada=jornada)
        return qs