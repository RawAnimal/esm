from rest_framework.viewsets import ModelViewSet

from .models import Country, Province, City
from .serializers import CountrySerializer, ProvinceSerializer, CitySerializer


class CountryViewSet(ModelViewSet):
    """
    Endpoint for viewing and editing countries.
    """

    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class ProvinceViewSet(ModelViewSet):
    """
    Endpoint for viewing and editing provinces.
    """

    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer


class CityViewSet(ModelViewSet):
    """
    Endpoint for viewing and editing cities.
    """

    queryset = City.objects.all()
    serializer_class = CitySerializer
