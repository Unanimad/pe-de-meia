from rest_framework import serializers

from .models import Ciclo


class CicloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciclo
        fields = '__all__'
        depth = 1
