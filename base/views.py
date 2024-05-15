from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Post

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class CarPageView(ListView):
    model = Post
    posts = Post.objects.all()
    template_name = 'pages/car_list.html'

class CarDetailView(TemplateView):
    template_name = 'pages/car_detail.html'

class NewsPageView(TemplateView):
    template_name = 'pages/news.html'

class Contact(TemplateView):
    template_name = 'pages/contact.html'