import urllib3
import json
import time
from weather.models import ForecastModel

open_weather_key = 'e4f710f948b2defa7ebb874a2e804d4a'

def get_weather_data(city):

    table_dict = {}
    temperature_dict = {}
    result_json = {}
    pressure_list = []
    temperature_list = []

    http = urllib3.PoolManager()
    api_key = open_weather_key
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q='
    locality = city.replace(' ', '%20')
    final_url = url + locality + '&mode=json&units=metric&cnt=' + str(14) + '&APIkey=' + api_key
    json_obj = http.request('GET', final_url)
    data = json.loads(json_obj.data.decode('utf-8'))

    # Table info

    table_dict['name'] = data['city']['name']
    table_dict['coordinates'] = data['city']['coord']
    table_dict['date'] = time.strftime('%Y-%m-%d', time.localtime(data['list'][0]['dt']))
    table_dict['pressure'] = data['list'][0]['pressure']
    table_dict['clouds'] = data['list'][0]['clouds']
    table_dict['wind'] = data['list'][0]['speed']
    table_dict['pressure'] = data['list'][0]['pressure']
    table_dict['min_temp'] = data['list'][0]['temp']['min']
    table_dict['max_temp'] = data['list'][0]['temp']['max']
    table_dict['description'] = data['list'][0]['weather'][0]['description']

    # Pressure info

    for i in range(0, 14):
         pressure_list.append(data['list'][i]['pressure'])
         temperature_list.append(time.strftime('%Y-%m-%d', time.localtime(data['list'][i]['dt'])))

    pressure_dict = dict(zip(temperature_list, pressure_list))

    # Temperature info

    temperature_dict['day'] = data['list'][0]['temp']['day']
    temperature_dict['night'] = data['list'][0]['temp']['night']
    temperature_dict['evening'] = data['list'][0]['temp']['eve']
    temperature_dict['morning'] = data['list'][0]['temp']['morn']

    result_json['table'] = table_dict
    result_json['pressure'] = pressure_dict
    result_json['temperature'] = temperature_dict

    # Saving/getting

    forecast = ForecastModel.objects.create(forecast_json=result_json)
    item = ForecastModel.objects.order_by('-id')[0]
    result_obj = item.forecast_json

    return result_obj


