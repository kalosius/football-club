from django.shortcuts import render

# Create your views here.
def home(request):
    pr_title = 'Mazowezo'
    return render(request, 'index.html', {'pr_title':pr_title})


def matches(request):
    return render(request, 'matches.html')


def news(request):
    return render(request, 'news.html')


def partners(request):
    return render(request, 'partners.html')


def players(request):
    return render(request, 'players.html')


def stadium(request):
    return render(request, 'stadium.html')