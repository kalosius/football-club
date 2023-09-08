import django_filters
from . models import Player

class Product_filter(django_filters.FilterSet):
    class Meta:
        model = Player
        fields = ['player_name']