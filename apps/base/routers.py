from rest_framework.routers import DefaultRouter
from apps.sig.routers import router as sig_router
from apps.sig.viewsets import PessoaViewSet
from apps.validador.routers import router as validador_routers

router = DefaultRouter()
# router.register(r'pessoa', PessoaViewSet, basename='pessoa')

router.registry.extend(validador_routers.registry)
