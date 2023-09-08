from django.shortcuts import render
from . models import *
from . filters import Product_filter
# Create your views here.
def home(request):
    return render(request, 'index.html')

def matches(request):
    return render(request, 'matches.html')


def news(request):
    return render(request, 'news.html')


def partners(request):
    return render(request, 'partners.html')


def players(request):
    players = Player.objects.all().order_by('-id')
    product_filter = Product_filter(request.GET, queryset=players)
    players = product_filter.qs
    return render(request, 'players.html', {'players':players,'product_filter':product_filter})


def stadium(request):
    return render(request, 'stadium.html')