from rest_framework import serializers

from car.models import Car


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'id',
            'model',
            'color',
            'dealers',
            'picture',
            'is_published',
            'price',
            'engine_type',
            'capacity',
            'gear_case',
            'doors',
            'property',
        ]
