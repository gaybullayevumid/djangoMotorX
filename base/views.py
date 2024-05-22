from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Product

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

# class CarPageView(TemplateView):
#     template_name = 'pages/car_list.html'

def carPageView(request):
    template_name = 'pages/car_list.html'
    cars = Product.objects.all()
    context = {'cars':cars}
    return render(request=request, template_name=template_name, context=context)


def carDetailView(request, pk):
    template_name = 'pages/car_detail.html'
    car = Product.objects.get(pk=pk)
    context = {'car':car}
    return render(request=request, template_name=template_name, context=context)


def newsPageView(request):
    template_name = 'pages/news.html'
    posts = Post.objects.all()
    p = Paginator(posts, 3)
    page_number = request.GET.get('page')
    # page_number = p.num_pages * "p"
    try:
        posts = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        posts = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        posts = p.page(p.num_pages)
    context = {'posts': posts}
    return render(request=request, template_name=template_name, context=context)

def newsDetailView(request, pk):
    template_name = 'pages/news_detail.html'
    post = Post.objects.get(pk=pk)
    context = {'post':post}
    return render(request=request, template_name=template_name, context=context)

class Contact(TemplateView):
    template_name = 'pages/contact.html'