from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('matches/', views.matches, name='matches'),
    path('news/', views.news, name='news'),
    path('partners/', views.partners, name='partners'),
    path('players/', views.players, name='players'),
    path('stadium/', views.stadium, name='stadium'),
]