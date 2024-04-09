from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Ciclo
from .serializers import CicloSerializer


class CicloViewSet(viewsets.ModelViewSet):
    queryset = Ciclo.objects.all()
    serializer_class = CicloSerializer
