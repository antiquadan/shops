from .models import (City, Street, Shop)
from rest_framework import generics
from .serial import (CitySerialize, StreetSerialize,ShopSerialize)

class CityListView(generics.ListAPIView):
    #queryset = City.objects.all().order_by('name')
    queryset = City.objects.all()
    serializer_class = CitySerialize

class CityDetailView(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerialize

class StreetListView(generics.ListAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerialize

class StreetDetailView(generics.RetrieveAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerialize

