from rest_framework import viewsets

from api.models import Factory, Sprocket
from api.serializers import FactoryDataSerializer, SprocketSerializer


class FactoryDataViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactoryDataSerializer


class SprocketViewSet(viewsets.ModelViewSet):
    queryset = Sprocket.objects.all()
    serializer_class = SprocketSerializer
