from rest_framework import routers

from apps.sig.viewsets import PessoaViewSet

app_name = 'sig'

router = routers.DefaultRouter()
# router.register(r'pessoa', PessoaViewSet, basename='pessoa')
