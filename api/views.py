from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from car.models import Car
from .serializers.car_serializer import CarModelSerializer


class CarView(viewsets.ViewSet):
    """
    A simple ViewSet that for listing or retrieving users.
    """

    def list(self, request):
        queryset = Car.objects.all()
        serializer = CarModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Car.objects.all().select_related('picture')
        user = get_object_or_404(queryset, pk=pk)
        serializer = CarModelSerializer(user)
        return Response(serializer.data)
