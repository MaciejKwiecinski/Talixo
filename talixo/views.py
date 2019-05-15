from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from talixo.models import CarInformations,CarList
from talixo.serializers import CarListSerializer,CarInformationsSerializer


class CarListView(generics.ListCreateAPIView):
    lookup_field = 'id'
    serializer_class = CarListSerializer
    queryset = CarList.objects.all()

class CarInformationsView(generics.ListCreateAPIView):
    lookup_field = 'id'
    serializer_class = CarInformationsSerializer
    queryset = CarInformations.objects.all()

class DocsView(APIView):
    def get(self,request):
            apidocs = {
                   'Car Create and List ': request.build_absolute_uri('car-list'),
                   'Car Informations Create and List': request.build_absolute_uri('car-info'),
                   'RUD Car':request.build_absolute_uri('rud-car/1'),
                   'RUD Informations':request.build_absolute_uri('rud-info/1'),
                   'If you want to do put, patch or delete any car or informations wrote add id to "rud-car/" or "rud-info/"':(),
                   }
            return Response(apidocs)

class RUDCarView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = CarListSerializer
    queryset = CarList.objects.all()

class RUDInformationsView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = CarInformationsSerializer
    queryset = CarInformations.objects.all()
