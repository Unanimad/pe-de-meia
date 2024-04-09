from django.db import models


class Incentivo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()


class TipoCiclo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)


class Ciclo(models.Model):
    nome = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    tipo = models.ForeignKey(TipoCiclo, on_delete=models.PROTECT)


class InconsistenciaCiclo(models.Model):
    cpf = models.IntegerField()
    etapa = models.CharField(max_length=2)
    situacao = models.CharField(max_length=12)
    descricao = models.TextField()

    ciclo = models.ForeignKey(Ciclo, on_delete=models.PROTECT)

    class Meta:
        unique_together = (('cpf', 'etapa', 'ciclo'),)
