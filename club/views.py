from django.shortcuts import render
from . models import *
from . filters import Product_filter
# Create your views here.
def home(request):
    players = Player.objects.all()
    return render(request, 'index.html', {'players':players})

def matches(request):
    return render(request, 'matches.html')


def news(request):
    return render(request, 'news.html')


def partners(request):
    return render(request, 'partners.html')


def players(request):
    # players = Player.objects.all().order_by('-id')
    # product_filter = Product_filter(request.GET, queryset=players)
    # players = product_filter.qs
    search_term = request.GET.get('player_name__search_term', 'player_name')
    # Perform data filtering based on the search_term
    filtered_players = Player.objects.filter(player_name__icontains=search_term)
    players = Player.objects.all()
    context = {
        'filtered_players': filtered_players,
        'players':players,
    }
    
    return render(request, 'players.html', context)

    # return render(request, 'players.html', {'players':players,'product_filter':product_filter})


def stadium(request):
    return render(request, 'stadium.html')

def player_view(request):
    return render(request, 'player_details.html')