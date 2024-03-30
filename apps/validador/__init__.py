from typing import Dict

from django.db.models import QuerySet

"""
Portaria: https://www.in.gov.br/web/dou/-/portaria-n-84-de-7-de-fevereiro-de-2024-542258771
"""


class PeMeiaEstudante:
    """
    Campos disponiveis no manual https://www.gov.br/mec/pt-br/pe-de-meia/manualSGP.pdf
    """
    cols = {
        'ESTUDANTE_CPF',
        'ESTUDANTE_NOME',
        'ESTUDANTE_DT_NASCIMENTO',
        'ESTUDANTE_MAE_NOME',
        'CO_ENTIDADE',
        'NO_ENTIDADE',
        'ESTUDANTE_ETAPA DE ENSINO',
        'MATRICULA_ATE_DOIS_MESES_DO_INICIO'
    }

    def __init__(self, qs: QuerySet):
        self.qs = qs

    @classmethod
    def __ha_registros(cls, qs: QuerySet):
        total = qs.count()
        if total > 0:
            return total
        return 0

    def valide(self) -> Dict:
        valida_methods = [func.replace('valida_', '') for func in dir(self) if callable(getattr(self, func))
                          if func.startswith('valida')]

        return {method: getattr(self, f'valida_{method}')() for method in valida_methods}

    def valida_cpfs_nulos(self):
        qs = self.qs.filter(cpf__isnull=True)
        return self.__ha_registros(qs)

    def valida_nomes_maes_nulos(self):
        qs = self.qs.filter(nome_mae__isnull=True)
        return self.__ha_registros(qs)

    def valida_menores_anos(self, idade: int = 14):
        qs = self.qs.filter(idade__lt=idade)
        return self.__ha_registros(qs)


class PeMeiaFrequencia:
    """
    Manual: https://www.gov.br/mec/pt-br/pe-de-meia/manual-de-envio-dos-dados-ao-sistema-presente-frequencia

    Frequência mínima mensal de 80% das horas letivas ou média de frequência de 80% das horas
    letivas no ano, até o momento da coleta da informação

    Retirado do arquiv: https://docs.google.com/spreadsheets/d/1iICnmwSQ9R5Zt97SGfCKLDkLTYmrFVdEth3ZAV5C6DM/edit#gid=591279922
    28/03/2024
    """
    cols = {
        'ESTUDANTE_CPF',
        'ESTUDANTE_NU_NIS',
        'ESTUDANTE_NOME',
        'CO_ENTIDADE',
        'NO_ENTIDADE',
        'ESTUDANTE_ETAPA_DE_ENSINO',
        'MES_REFERENCIA	ANO_REFERENCIA',
        'HL_OFERTADA_PERIODO',
        'HL_PRESENTE_PERIODO',
        'JUSTIFICATIVA',
    }


class PeMeiaConclusao:
    """
    Conclusão da série em que está matriculado, com aprovação e, quando for o caso,
    participação nos exames do Saeb, e nos exames aplicados pelos sistemas de avaliação
    externa dos entes federativos para o ensino médio
    """
    ...


class PeMeiaEnem:
    """
    Inscrição e participação nos dois dias de realização do Exame Nacional do Ensino Médio - Enem,
    incluindo eventual reaplicação nas situações de excepcionalidade
    """
    ...
