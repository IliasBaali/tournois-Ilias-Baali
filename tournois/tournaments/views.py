from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404,HttpResponse
from .models import Tournoi

# Create your views here.
def tournois(request):
    tournois_list = get_list_or_404(Tournoi)
    return render(request, 'tournaments/tournois.html', {'tournois_list': tournois_list})