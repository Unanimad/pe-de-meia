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
        validacao = PeMeiaEstudante(qs).valide()

        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(qs, request)

        serializer = self.serializer_class(paginated_queryset, many=True)
        data = {
            'count': paginator.count,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link(),
            'results': serializer.data,
            **validacao
        }
        return Response(data, status=status.HTTP_200_OK)
