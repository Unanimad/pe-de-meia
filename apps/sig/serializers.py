from rest_framework import serializers

from apps.sig.models.comum import SigPessoa


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SigPessoa
        fields = '__all__'
