from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('car_list/', CarPageView.as_view(), name='car_list'),
    path('car_detail/', CarDetailView.as_view(), name='car_detail'),
    path('news/', views.newsPageView, name='news'),
    path('news_detail/<int:pk>/', views.newsDetailView, name='news_detail'),
    path('contact/', Contact.as_view(), name='contact'),
]