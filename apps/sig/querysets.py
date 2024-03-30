from django.utils import timezone
from django.db import models
from django.db.models import F, Count, When, Value, IntegerField, Case, OuterRef, Subquery, Func, CharField

from apps.sig.models.ensino import SigDiscente, SigDiscenteTurma
from apps.sig.models.tecnico import SigCursoTecnico  # se remover essa linha para de funcionar!


class SigDiscenteQuerySet(models.QuerySet):

    def pe_meia(self) -> models.QuerySet:
        count_ano = Count('ano', distinct=True)
        subquery_situacao_2 = Subquery(
            SigDiscenteTurma.objects.filter(
                discente_id=OuterRef('id'), situacao_matricula_id=2
            ).values('discente_id').annotate(
                contador_ano=count_ano
            ).values('contador_ano')[:1]
        )

        subquery_situacao_4 = Subquery(
            SigDiscenteTurma.objects.filter(
                discente_id=OuterRef('id'), situacao_matricula_id=4
            ).values('discente_id').annotate(
                contador_ano=count_ano
            ).values('contador_ano')[:1]
        )

        etapa_ensino = Case(
            When(contador_ano__lte=1, then=Value(30)),
            When(contador_ano=2, then=Value(31)),
            When(contador_ano=3, then=Value(32)),
            When(contador_ano__gte=4, then=Value(33)),
            When(curso__sigcursotecnico__regime_academico=2, then=Value(34)),
            default=Value(34), output_field=IntegerField(),
        )

        queryset = SigDiscente.objects.select_related(
            'pessoa', 'curso', 'curso__campus'
        ).prefetch_related(
            'sigdiscenteturma_set'
        ).annotate(
            cpf=F('pessoa__cpf_cnpj'),
            nome=F('pessoa__nome'),
            data_nascimento=Func(F('pessoa__data_nascimento'), Value('DD/MM/YYYY'), function='to_char',
                                 output_field=CharField()),
            nome_mae=F('pessoa__nome_mae'),
            contador_ano=(subquery_situacao_2 + subquery_situacao_4)
        ).annotate(
            idade=Func(
                Value('year'), Func(
                    Value(timezone.now().date()), F('pessoa__data_nascimento'), function='age'
                ), function='date_part', output_field=IntegerField()
            ),
            etapa_ensino=etapa_ensino
        ).filter(
            nivel__in=['T', 'M'],
            status_discente_id=1
        ).order_by('curso__campus__nome', 'pessoa__nome').values(
            'cpf', 'nome', 'data_nascimento', 'nome_mae', 'etapa_ensino', 'idade'
        )

        return queryset
