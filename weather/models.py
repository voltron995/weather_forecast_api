from django.db import models
from jsonfield import JSONField


class ForecastModel(models.Model):
    id = models.AutoField(primary_key=True)
    forecast_json = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)