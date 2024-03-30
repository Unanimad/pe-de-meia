from rest_framework import viewsets, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from apps.base.serializers import EntidadeSerializer
from apps.sig.querysets import SigDiscenteQuerySet
from apps.validador import PeMeiaEstudante

from apps.validador.serializers import EstudanteSerializer


class EstudanteViewSet(viewsets.ViewSet):
    serializer_class = EstudanteSerializer
    pagination_class = LimitOffsetPagination

    ENTIDADES = EntidadeSerializer(EntidadeSerializer.Meta.model.objects.all(), many=True).data

    def list(self, request, *args, **kwargs):
        paginator = self.pagination_class()
        query_params = self.request.query_params.dict()

        if query_params.get('limit'):
            query_params.pop('limit')
        if query_params.get('offset'):
            query_params.pop('offset')
        if query_params.get('format'):
            query_params.pop('format')

        qs = SigDiscenteQuerySet().pe_meia()
        qs = qs.filter(**query_params)

        validacao = PeMeiaEstudante(qs).valide()

        paginated_queryset = paginator.paginate_queryset(qs, request)
        serializer = self.serializer_class(paginated_queryset, many=True)

        data = {
            'count': paginator.count,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link(),
            'entidades': self.ENTIDADES,
            'results': serializer.data,
            'info': {**validacao}
        }

        return Response(data, status=status.HTTP_200_OK)
