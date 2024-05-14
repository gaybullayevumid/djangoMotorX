from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('car_list/', CarPageView.as_view(), name='car_list')
]