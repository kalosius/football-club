from django.contrib import admin
from . models import Player
# Register your models here.

class PlayerAdmin(admin.ModelAdmin):
    list_display = ['player_name', 'team', 'shirt_number', 'date_of_birth', 'player_image']

admin.site.register(Player, PlayerAdmin)

# 