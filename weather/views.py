from django.http import JsonResponse
from weather import services

def get_forecast(request, *args, **kwargs):
    data = services.get_weather_data(kwargs['city'])
    return JsonResponse(data)