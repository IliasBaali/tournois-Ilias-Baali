from django.contrib import admin
from .models import Tournoi,Poule,Team, Match

# Register your models here.
admin.site.register(Tournoi) 
admin.site.register(Poule)
admin.site.register(Team)
admin.site.register(Match)