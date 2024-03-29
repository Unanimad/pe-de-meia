from rest_framework.routers import DefaultRouter

from apps.validador.viewsets import EstudanteViewSet

router = DefaultRouter()
router.register(r'estudantes', EstudanteViewSet, basename='estudantes')
