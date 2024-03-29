from rest_framework.routers import DefaultRouter
from apps.sig.routers import router as sig_router
from apps.sig.viewsets import PessoaViewSet

router = DefaultRouter()
router.register(r'pessoa', PessoaViewSet, basename='pessoa')

# router.registry.extend(sig_router.registry)
