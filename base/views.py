from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Post

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class CarPageView(TemplateView):
    template_name = 'pages/car_list.html'


class CarDetailView(TemplateView):
    template_name = 'pages/car_detail.html'

def newsPageView(request):
    template_name = 'pages/news.html'
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request=request, template_name=template_name, context=context)

def newsDetailView(request, pk):
    template_name = 'pages/news_detail.html'
    post = Post.objects.get(pk=pk)
    context = {'post':post}
    return render(request=request, template_name=template_name, context=context)

class Contact(TemplateView):
    template_name = 'pages/contact.html'