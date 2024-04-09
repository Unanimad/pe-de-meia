from django.db import models


class Incentivo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class TipoCiclo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Ciclo(models.Model):
    nome = models.CharField(max_length=100)
    observacao = models.TextField(blank=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    tipo = models.ForeignKey(TipoCiclo, on_delete=models.PROTECT)
    incentivo = models.ForeignKey(Incentivo, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class InconsistenciaCiclo(models.Model):
    cpf = models.CharField(max_length=11, db_index=True)
    etapa = models.CharField(max_length=2)
    situacao = models.CharField(max_length=12)
    descricao = models.TextField()

    ciclo = models.ForeignKey(Ciclo, on_delete=models.PROTECT)

    class Meta:
        unique_together = (('cpf', 'etapa', 'ciclo'),)
