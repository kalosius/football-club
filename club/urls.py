from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
import django

urlpatterns = [
    path('', views.home, name='home'),
    path('matches/', views.matches, name='matches'),
    path('news/', views.news, name='news'),
    path('partners/', views.partners, name='partners'),
    path('players/', views.players, name='players'),
    path('stadium/', views.stadium, name='stadium'),
    path('player_view/', views.player_view, name='player_view'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)