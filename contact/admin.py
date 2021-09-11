from django.contrib import admin

from contact import models

admin.site.register(models.Country)
admin.site.register(models.Province)
admin.site.register(models.City)
