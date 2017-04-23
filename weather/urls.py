from django.conf.urls import url, include
from weather import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
  url(r'^api/(?P<city>\w+)$', views.get_forecast, name='weather'),
]

urlpatterns = format_suffix_patterns(urlpatterns)