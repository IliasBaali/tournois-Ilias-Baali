from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404,HttpResponse
from .models import Tournoi, Poule, Match

# Create your views here.
def tournois(request):
    tournois_list = get_list_or_404(Tournoi)
    return render(request, 'tournaments/tournois.html', context_with_user(request,{'tournois_list': tournois_list}))

def tournoiDetail(request, tournament_id):
    tournament = get_object_or_404(Tournoi, pk=tournament_id)
    return render(request, 'tournaments/tournoi_detail.html', context_with_user(request,{'tournoi': tournament}))

def pouleDetail(request, pool_id):
    pool = get_object_or_404(Poule, pk=pool_id)
    return render(request, 'tournaments/poule_detail.html', context_with_user(request,{'poule': pool}))

def matchDetail(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    return render(request, 'tournaments/match_detail.html', context_with_user(request,{'match': match}))

def context_with_user(request, context):
    if request.user.is_authenticated:
        username = request.user.username
    else : 
        username = None
    context['username'] = username
    return context