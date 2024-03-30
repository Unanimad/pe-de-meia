from rest_framework import viewsets, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from apps.sig.querysets import SigDiscenteQuerySet
from apps.validador import PeMeiaEstudante

from apps.validador.serializers import EstudanteSerializer


class EstudanteViewSet(viewsets.ViewSet):
    serializer_class = EstudanteSerializer
    pagination_class = LimitOffsetPagination

    def list(self, request):
        qs = SigDiscenteQuerySet().pemeia()
        validacao = PeMeiaEstudante(qs).valida()

        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(qs, request)

        serializer = self.serializer_class(paginated_queryset, many=True)
        data = {'validacoes': validacao, 'estudantes': serializer.data}
        return Response(data, status=status.HTTP_200_OK)
