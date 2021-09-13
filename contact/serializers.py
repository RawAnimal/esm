from rest_framework import serializers

from .models import Country, Province, City


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class ProvinceSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()

    class Meta:
        model = Province
        fields = ["name", "abbr", "country"]


class CitySerializer(serializers.ModelSerializer):
    province = serializers.StringRelatedField()

    class Meta:
        model = City
        fields = ["name", "province"]
