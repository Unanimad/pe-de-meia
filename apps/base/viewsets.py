from rest_framework import viewsets

from apps.base.models import Entidade
from apps.base.serializers import EntidadeSerializer


class EntidadeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Entidade.objects.all()
    serializer_class = EntidadeSerializer
    permission_classes = []
