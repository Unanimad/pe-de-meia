import csv

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from django.http import HttpResponse
from django.utils import timezone

from apps.base.serializers import EntidadeSerializer
from apps.sig.querysets import SigDiscenteQuerySet
from apps.validador import PeMeiaEstudante
from apps.validador.serializers import EstudanteSerializer


class EstudanteViewSet(viewsets.ViewSet):
    serializer_class = EstudanteSerializer
    pagination_class = LimitOffsetPagination

    ENTIDADES = EntidadeSerializer(EntidadeSerializer.Meta.model.objects.all(), many=True).data

    def __get_qs(self, request):
        query_params = request.query_params.dict()

        if query_params.get('limit'):
            query_params.pop('limit')
        if query_params.get('offset'):
            query_params.pop('offset')
        if query_params.get('format'):
            query_params.pop('format')

        qs = SigDiscenteQuerySet().pe_meia()
        qs = qs.filter(**query_params)

        return qs

    def list(self, request, *args, **kwargs):
        paginator = self.pagination_class()
        qs = self.__get_qs(self.request)
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

    @action(detail=False, methods=['GET', ], name='Download planilha Pé-de-meia', url_path='download_csv',
            permission_classes=[])
    def download_csv(self, request):
        # if not request.user.is_superuser:
        #     return Response({'err': 'Você precisa ter permissões para executar essa ação.'}, status.HTTP_403_FORBIDDEN)
        response = HttpResponse(content_type='text/csv')
        hoje = timezone.now().date().strftime('%d_%m_%Y')
        response['Content-Disposition'] = f'attachment; filename="pe-de-meia-estudante-{hoje}.csv"'
        writer = csv.DictWriter(response, fieldnames=list(PeMeiaEstudante.cols))
        writer.writeheader()
        qs = self.__get_qs(request)
        serializer = self.serializer_class(qs, many=True)
        [writer.writerow(PeMeiaEstudante.parse(estudante, 'csv')) for estudante in serializer.data]

        return response
