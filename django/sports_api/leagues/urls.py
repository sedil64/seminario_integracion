from rest_framework.routers import DefaultRouter
from leagues.views.league import LeagueViewSet
from leagues.views.team import TeamViewSet

router = DefaultRouter()
router.register(r'leagues', LeagueViewSet, basename='league')
router.register(r'teams', TeamViewSet, basename='team')

urlpatterns = router.urls
