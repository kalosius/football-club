from django.contrib import admin
from . models import Player, Gallery
# Register your models here.

class PlayerAdmin(admin.ModelAdmin):
    list_display = ['player_name', 'team', 'shirt_number', 'date_of_birth', 'player_image']

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['gallery_pic']

admin.site.register(Player, PlayerAdmin)
admin.site.register(Gallery, GalleryAdmin)

# 