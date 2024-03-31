from rest_framework import viewsets
from rest_framework.response import Response

from apps.sig.models.comum import SigPessoa
from apps.sig.serializers import PessoaSerializer


class PessoaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SigPessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = []
