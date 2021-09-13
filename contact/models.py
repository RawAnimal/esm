from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=2)

    class Meta:
        db_table = "countries"
        ordering = ("name",)
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self) -> str:
        return self.name


class Province(models.Model):
    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=2)
    country = models.ForeignKey(
        Country, on_delete=models.PROTECT, related_name="province_country"
    )

    class Meta:
        db_table = "provinces"
        ordering = ("name",)
        verbose_name = "Province"
        verbose_name_plural = "Provinces"

    def __str__(self) -> str:
        return f"{self.name} {self.country.abbr}"


class City(models.Model):
    name = models.CharField(max_length=50)
    province = models.ForeignKey(
        Province, on_delete=models.PROTECT, related_name="city_province"
    )

    class Meta:
        db_table = "cities"
        ordering = ("name",)
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self) -> str:
        return f"{self.name} {self.province.abbr}"
