from rest_framework.routers import DefaultRouter
from leagues.views.liga import LigaViewSet
from leagues.views.equipo import EquipoViewSet
from leagues.views.jugador import JugadorViewSet
from leagues.views.partido import PartidoViewSet
from leagues.views.estadistica import EstadisticaJugadorViewSet
from leagues.views.tabla import TablaPosicionesViewSet

router = DefaultRouter()
router.register(r'ligas', LigaViewSet, basename='liga')
router.register(r'equipos', EquipoViewSet, basename='equipo')
router.register(r'jugadores', JugadorViewSet, basename='jugador')
router.register(r'partidos', PartidoViewSet, basename='partido')
router.register(r'estadisticas', EstadisticaJugadorViewSet, basename='estadistica')
router.register(r'tabla-posiciones', TablaPosicionesViewSet, basename='tabla')

urlpatterns = router.urls