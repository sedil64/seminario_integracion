from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views.admin import UserAdminViewSet
from users.views.auth import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'admin/users', UserAdminViewSet, basename='admin-users')

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
    path('', include(router.urls)),
]