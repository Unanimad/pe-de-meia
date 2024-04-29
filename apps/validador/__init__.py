from abc import ABC
from typing import Dict

from django.db.models import QuerySet

"""
Portaria: https://www.in.gov.br/web/dou/-/portaria-n-84-de-7-de-fevereiro-de-2024-542258771
"""


class PeMeia(ABC):
    cols = {}

    def __init__(self, qs: QuerySet):
        self.qs = qs

    @classmethod
    def _ha_registros(cls, qs: QuerySet):
        return qs.count()

    def valide(self) -> Dict:
        valida_methods = [func.replace('valida_', '') for func in dir(self) if callable(getattr(self, func))
                          if func.startswith('valida')]

        return {method: {
            'total': getattr(self, f'valida_{method}')(),
            'label': getattr(self, f'valida_{method}').__doc__.split(':')[0].strip(),
            'qs': getattr(self, f'valida_{method}').__doc__.split(':')[1].strip()
        }
            for method in valida_methods}

    def gera_csv(self):
        ...


class PeMeiaEstudante(PeMeia):
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

    def valida_cpfs_nulos(self):
        """
        CPFs nulos: cpf__isnull=True
        """
        qs = self.qs.filter(cpf__isnull=True)
        return self._ha_registros(qs)

    def valida_nomes_maes_nulos(self):
        """
        Sem nome de mãe: nome_mae__isnull=True
        """
        qs = self.qs.filter(nome_mae__isnull=True)
        return self._ha_registros(qs)

    def valida_menores_anos(self, idade: int = 14):
        """
        Com menos de 14 anos: idade__lt=14
        """
        qs = self.qs.filter(idade__lt=idade)
        return self._ha_registros(qs)

    def valida_maiores_anos(self, idade: int = 24):
        """
        Maior de 24 anos até 31/03: idade__gte=24&data_nascimento__lte='2000-31-03'
        """
        data_nascimento_limite = '2000-31-03'
        qs = self.qs.filter(idade__gte=idade, data_nascimento__lte=data_nascimento_limite)
        return self._ha_registros(qs)

    @classmethod
    def parse(cls, estudante: Dict, type_='csv') -> Dict:
        return {
            'ESTUDANTE_CPF': estudante.get('cpf', ''),
            'ESTUDANTE_NOME': estudante.get('nome', ''),
            'ESTUDANTE_DT_NASCIMENTO': estudante.get('data_nascimento', ''),
            'ESTUDANTE_MAE_NOME': estudante.get('nome_mae', ''),
            'CO_ENTIDADE': estudante.get('', ''),
            'NO_ENTIDADE': estudante.get('', ''),
            'ESTUDANTE_ETAPA DE ENSINO': estudante.get('etapa_ensino', ''),
            'MATRICULA_ATE_DOIS_MESES_DO_INICIO': estudante.get('', ''),
        }


class PeMeiaFrequencia(PeMeia):
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


class PeMeiaConclusao(PeMeia):
    """
    Conclusão da série em que está matriculado, com aprovação e, quando for o caso,
    participação nos exames do Saeb, e nos exames aplicados pelos sistemas de avaliação
    externa dos entes federativos para o ensino médio
    """
    ...


class PeMeiaEnem(PeMeia):
    """
    Inscrição e participação nos dois dias de realização do Exame Nacional do Ensino Médio - Enem,
    incluindo eventual reaplicação nas situações de excepcionalidade
    """
    ...
