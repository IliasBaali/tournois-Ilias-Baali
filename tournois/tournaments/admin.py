from django.contrib import admin
from .models import Tournoi,Poule,Team

# Register your models here.
admin.site.register(Tournoi) 
admin.site.register(Poule)
admin.site.register(Team)