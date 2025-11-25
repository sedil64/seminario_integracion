from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('leagues.urls')),
    path('api/', include('matches.urls')),  # ahora /api/matches/
]
