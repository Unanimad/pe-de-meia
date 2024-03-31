from django.db import models

from apps.sig.models.comum import SigPessoa


class SigCategoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = u'"rh\".\"categoria"'
        default_permissions = ()


class SigServidor(models.Model):
    id_servidor = models.IntegerField(primary_key=True)
    siape = models.IntegerField()
    id_ativo = models.IntegerField()
    pessoa = models.ForeignKey(SigPessoa, on_delete=models.RESTRICT, db_column='id_pessoa')
    categoria = models.ForeignKey(SigCategoria, on_delete=models.RESTRICT, db_column='id_categoria')

    class Meta:
        managed = False
        db_table = u'"rh\".\"servidor"'
        default_permissions = ()