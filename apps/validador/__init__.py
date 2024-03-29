import pandas as pd

"""
Portaria: https://www.in.gov.br/web/dou/-/portaria-n-84-de-7-de-fevereiro-de-2024-542258771
"""


class PeMeiaEstudante:
    """
    Campos disponiveis no manual https://www.gov.br/mec/pt-br/pe-de-meia/manualSGP.pdf
    """
    cols = {
        'ESTUDANTE_CPF',
        'ESTUDANTE_NU_NIS',
        'ESTUDANTE_NOME',
        'ESTUDANTE_DT_NASCIMENTO',
        'ESTUDANTE_MAE_NOME',
        'CO_ENTIDADE',
        'NO_ENTIDADE',
        'ESTUDANTE_ETAPA DE ENSINO',
        'MATRICULA_ATE_DOIS_MESES_DO_INICIO'
    }

    def __init__(self, df: pd.DataFrame):
        self.df = df

    @classmethod
    def apenas_numeros(cls, texto: str) -> str:
        """
        remove caracteres alpha
        :param texto: ESTUDANTE_NU_RG, ESTUDANTE_CPF...
        :return: somente numeros
        """
        return ''.join([c for c in texto if c.isdigit()])

    def validador_cpf(self):
        # TODO: Precisa retornar quantos estão invalidos e quais são (se houver)
        cpfs = self.df['ESTUDANTE_CPF'].apply(self.apenas_numeros)

    def validador_nis(self):
        # TODO: Obrigatório caso não tenha CPF
        ...

    def validador_estudante_nome(self):
        # TODO: há nomes vazios ou incompletos?
        nomes = self.df['ESTUDANTE_NOME'].apply(lambda row: row.strip()[:150])

    def validador_dt_nascimento(self):
        dts_nascimento = self.df['ESTUDANTE_DT_NASCIMENTO']
        # TODO > 14 anos

    def validador_mae_nome(self):
        maes_nomes = self.df['ESTUDANTE_MAE_NOME'].apply(lambda row: row.strip()[:150])

    def validador_entidade(self):
        # TODO: precisa pegar do modelo base as informacoes do codigo e nome
        ...

    def validador_codigo_ensino(self):
        # de onde tem os códigos?
        ...

    def validador_etapa_ensino(self):
        ...

    def validador_matricula_dois_meses_inicio(self):
        ...


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
