from rest_framework.routers import DefaultRouter

from apps.base.viewsets import EntidadeViewSet
from apps.validador.routers import router as validador_routers

router = DefaultRouter()
router.register(r'entidades', EntidadeViewSet, basename='entidades')

router.registry.extend(validador_routers.registry)
