from rest_framework import serializers

from apps.base.serializers import EntidadeSerializer


class ValidadorSerializer(serializers.ModelSerializer):
    campo = serializers.CharField()
    valido = serializers.BooleanField()
    mensagem = serializers.CharField()


class EstudanteSerializer(serializers.Serializer):
    # 'cpf', 'nome', 'data_nascimento', 'nome_mae', 'etapa_ensino',
    cpf = serializers.CharField(max_length=11)
    nome = serializers.CharField()
    data_nascimento = serializers.DateField()
    nome_mae = serializers.CharField()
    etapa_ensino = serializers.IntegerField()
    # matricula_dois_meses_inicio = serializers.BooleanField()
    # entidade = EntidadeSerializer()
    # validado = ValidadorSerializer(many=True)
