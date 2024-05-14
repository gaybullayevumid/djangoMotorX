from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class CarPageView(TemplateView):
    template_name = 'pages/car_list.html'