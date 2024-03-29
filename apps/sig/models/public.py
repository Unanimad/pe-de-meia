from django.db import models

from apps.sig.models.comum import SigCampus, SigPessoa


class SigStatusDiscente(models.Model):
    id = models.AutoField(primary_key=True, db_column='status')
    descricao = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'status_discente'
        default_permissions = ()


class SigDiscente(models.Model):
    id = models.AutoField(primary_key=True, db_column='id_discente')
    matricula = models.PositiveBigIntegerField()
    pessoa = models.ForeignKey(SigPessoa, on_delete=models.RESTRICT, db_column='id_pessoa')
    status_discente = models.ForeignKey(SigStatusDiscente, on_delete=models.RESTRICT, db_column='status')
    ano_ingresso = models.PositiveSmallIntegerField(db_column='ano_ingresso')
    periodo_ingresso = models.PositiveSmallIntegerField(db_column='periodo_ingresso')
    curso = models.ForeignKey('SigCurso', on_delete=models.RESTRICT, db_column='id_curso')

    class Meta:
        managed = False
        db_table = 'discente'
        default_permissions = ()


class SigCurso(models.Model):
    id = models.AutoField(primary_key=True, db_column='id_curso')
    nome = models.CharField(max_length=200)
    nivel = models.CharField(max_length=1)
    ativo = models.BooleanField(db_column='ativo')
    campus = models.ForeignKey(SigCampus, on_delete=models.RESTRICT, db_column='id_unidade')

    class Meta:
        managed = False
        db_table = 'curso'
        default_permissions = ()

    def __str__(self):
        return self.nome
