from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('car_list/', CarPageView.as_view(), name='car_list'),
    path('car_detail/', CarDetailView.as_view(), name='car_detail'),
    path('news/', NewsPageView.as_view(), name='news'),
    path('contact/', Contact.as_view(), name='contact')
]