from django.db import models

from apps.sig.models.comum import SigCampus


class Entidade(models.Model):
    """
    Planilha - Entidades Instituto Federal
    3183/2981	Instituto Federal de Sergipe - Campus Aracaju
    32011	Instituto Federal de Sergipe - Campus Socorro
    3046	Instituto Federal de Sergipe - Campus São Cristóvão
    20063	Instituto Federal de Sergipe - Campus Itabaiana
    32013	Instituto Federal de Sergipe - Campus Propriá
    32015	Instituto Federal de Sergipe - Campus Tobias Barreto
    20078	Instituto Federal de Sergipe - Campus Nossa Senhora da Glória
    20064	Instituto Federal de Sergipe - Campus Estância
    3445	Instituto Federal de Sergipe - Campus Lagarto
    3237	Instituto Federal de Sergipe - Campus Poço Redondo
    """
    codigo = models.CharField('Código', max_length=9)
    nome = models.TextField('Nome')

    # TODO: necessário codigo municipio
    campus = models.PositiveBigIntegerField(unique=True)  # id_unidade de SigCampus


class TipoCodigo(models.Model):
    """
    Sistec, educacenso...
    """
    nome = models.CharField(max_length=10)


class CodigoEntidade(models.Model):
    codigo = models.CharField('Código', max_length=8)

    entidade = models.ForeignKey(Entidade, models.PROTECT)
    tipo_codigo = models.ForeignKey(TipoCodigo, models.PROTECT)
