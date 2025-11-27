from rest_framework import viewsets, filters
from leagues.models import Jugador
from leagues.serializers.jugador import JugadorSerializer
from leagues.permissions import IsAdminOrReadOnly
from leagues.pagination import StandardResultsSetPagination

class JugadorViewSet(viewsets.ModelViewSet):
    queryset = Jugador.objects.select_related('equipo').all()
    serializer_class = JugadorSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('nombre', 'apellido', 'nacionalidad', 'posicion')
    ordering_fields = ('apellido', 'nombre', 'numero_camiseta')

    def get_queryset(self):
        qs = super().get_queryset()
        equipo = self.request.query_params.get('equipo')
        posicion = self.request.query_params.get('posicion')
        if equipo:
            qs = qs.filter(equipo__id=equipo)
        if posicion:
            qs = qs.filter(posicion=posicion)
        return qs