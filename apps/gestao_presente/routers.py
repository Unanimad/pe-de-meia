from rest_framework.routers import DefaultRouter

from .viewsets import CicloViewSet

router = DefaultRouter()
router.register(r'ciclos', CicloViewSet, basename='ciclos')
