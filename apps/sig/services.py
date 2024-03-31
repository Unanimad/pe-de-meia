from django.core.exceptions import ObjectDoesNotExist

from apps.base.utils import encrypt_password

from apps.sig.models.comum import SigUsuario, SigPessoa
from apps.sig.models.public import SigStatusDiscente, SigDiscente
from apps.sig.models.rh import SigServidor


class SigService:

    def autentica_sig(self, usuario, senha) -> SigUsuario:
        try:
            senha = encrypt_password(senha)
            query_base = SigUsuario.objects.filter(login=usuario, senha=senha)
            if query_base.exists():
                return query_base.first()

            raise ObjectDoesNotExist("Credenciais inválidas na Plataforma SIG")
        except ObjectDoesNotExist as exception:
            raise exception

    def get_categorias_pessoa(self, pessoa: SigPessoa) -> []:
        """Busca vinculos ativos de professores, alunos e tecnicos administrativo"""
        try:
            retorno = []
            status_discente_ativos = SigStatusDiscente.objects.filter(
                descricao__in=['ATIVO', 'ATIVO - FORMANDO', 'ATIVO - GRADUANDO']
            ).values_list('descricao', flat=True)

            query_base = SigServidor.objects.filter(pessoa=pessoa, id_ativo__in=[1, 7])
            for row in query_base:
                categoria = row.categoria
                retorno.append(categoria.descricao.strip())

            query_base = SigDiscente.objects.filter(
                pessoa=pessoa,
                status_discente__descricao__in=status_discente_ativos
            )

            if query_base.exists():
                retorno.append('Discente')

            if len(retorno) > 0:
                return retorno
            raise ObjectDoesNotExist("Categoria não encontrada na plataforma SIG")
        except ObjectDoesNotExist as exception:
            raise exception
