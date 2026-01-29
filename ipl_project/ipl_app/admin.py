from django.contrib import admin
from .models import Franchise, Player, stadium

# Register your models here.
admin.site.register(Franchise)
admin.site.register(Player)
admin.site.register(stadium)