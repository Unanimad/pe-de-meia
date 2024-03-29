import hashlib
import base64

from datetime import timedelta, date

from django.conf import settings
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def encrypt_password(password):
    """
    Converte a string da senha, informada no formulário de autenticação, para o padrão do banco de dados Sig
    :param password: string
    :return: string da senha em hex md5
    """
    return hashlib.md5(password.encode('utf')).hexdigest()


def open_file(file_name):
    """
    Abra e leia o arquivo informado
    :param file_name: nome do arquivo
    :type file_name: string
    :return: conteúdo do arquivo
    :rtype: string
    """
    with open(file_name, encoding='utf-8') as file:
        return file.read()


def get_idade(data):
    """
    Calcule a idade a partir da data de nascimento
    :param data: data de nascimento
    :type data: date
    :return: idade
    :rtype: int
    """
    return (date.today() - data) // timedelta(days=365.2425)


def request_is_post(request):
    return request.method == 'POST'


def request_is_get(request):
    return request.method == 'GET'


def paginacao(request, registros, qtd_registro=settings.PAGINACAO_REGISTRO_POR_PAGINA):
    paginator = Paginator(registros, qtd_registro)
    page = request.GET.get('page')
    try:
        resultado_com_paginacao = paginator.page(page)
    except PageNotAnInteger:
        resultado_com_paginacao = paginator.page(1)
    except EmptyPage:
        resultado_com_paginacao = paginator.page(paginator.num_pages)

    return resultado_com_paginacao


def query_set_to_json(queryset):
    return serializers.serialize('json', queryset)


def make_hash_sha256(o):
    hasher = hashlib.sha256()
    hasher.update(repr(make_hashable(o)).encode())
    return base64.b64encode(hasher.digest()).decode()


def make_hashable(o):
    if isinstance(o, (tuple, list)):
        return tuple((make_hashable(e) for e in o))

    if isinstance(o, dict):
        return tuple(sorted((k, make_hashable(v)) for k, v in o.items()))

    if isinstance(o, (set, frozenset)):
        return tuple(sorted(make_hashable(e) for e in o))

    return o
