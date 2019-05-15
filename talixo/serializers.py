from rest_framework import serializers
from talixo.models import CarList, CarInformations


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarList
        fields = '__all__'


class CarInformationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarInformations
        fields = '__all__'