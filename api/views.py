from typing import Any
from rest_framework import viewsets, mixins
from rest_framework.request import Request
from rest_framework.response import Response

from api.models import Factory, Sprocket
from api.serializers import FactorySerializer, SprocketSerializer


class FactoryViewSet(viewsets.ModelViewSet):
    """
    This viewset is a RESTful view that allows to show factories with the chart data
    """

    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class SprocketViewSet(viewsets.ModelViewSet):
    """
    This viewset is a RESTful view shows sprocket data
    """

    queryset = Sprocket.objects.all()
    serializer_class = SprocketSerializer


class SprocketFactoryViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    This viewset is a list view that gets sprockets for a given factory id
    """

    queryset = Factory.objects.all()
    serializer_class = SprocketSerializer

    def retrieve(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Custom retrieve method to retrieve a factory's sprockets
        """

        instance = self.get_object()

        queryset = Sprocket.objects.filter(factory=instance)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
