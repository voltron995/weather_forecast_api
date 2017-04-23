from django.contrib import admin

# Register your models here.
from weather.models import ForecastModel

admin.site.register(ForecastModel)