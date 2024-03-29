from django.db import models


class SigPessoa(models.Model):
    id_pessoa = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    cpf_cnpj = models.BigIntegerField()
    data_nascimento = models.DateField()
    nome_mae = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = u'"comum\".\"pessoa"'
        default_permissions = ()


class SigPessoaNecessidadeEspecial(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id_pessoa_necessidade_especial')
    observacao = models.TextField()
    necessidade_especial = models.ForeignKey('SigTipoNecessidadeEspecial', models.RESTRICT,
                                             db_column='id_necessidade_especial')
    pessoa = models.ForeignKey(SigPessoa, models.RESTRICT, db_column='id_pessoa')

    class Meta:
        managed = False
        db_table = u'"comum\".\"pessoa_necessidade_especial"'
        default_permissions = ()


class SigTipoNecessidadeEspecial(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id_tipo_necessidade_especial')
    descricao = models.TextField(db_column='descricao')

    class Meta:
        managed = False
        db_table = u'"comum\".\"tipo_necessidade_especial"'
        default_permissions = ()


class SigUsuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=20)
    senha = models.CharField(max_length=60)
    pessoa = models.ForeignKey(SigPessoa, on_delete=models.RESTRICT, db_column='id_pessoa')

    class Meta:
        managed = False
        db_table = u'"comum\".\"usuario"'
        default_permissions = ()


class SigCampus(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id_unidade')
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = u'"comum\".\"unidade"'
        default_permissions = ()
