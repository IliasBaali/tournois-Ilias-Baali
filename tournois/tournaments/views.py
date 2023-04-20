from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.http import Http404,HttpResponseRedirect
from .models import Tournoi, Poule, Match, Commentaire
from .forms import CommentForm
from django.utils import timezone

def context_with_user(request, context):
    "Method that adds the username of a connected user to the specified context"
    if request.user.is_authenticated:
        username = request.user.username
    else : 
        username = None
    context['username'] = username
    return context

# Create your views here.
def tournois(request):
    """
    Get all tournaments from database
    :param request: The incoming request
    """
    tournois_list = get_list_or_404(Tournoi)
    return render(request, 'tournaments/tournois.html', context_with_user(request,{'tournois_list': tournois_list}))

def tournoiDetail(request, tournament_id):
    """
    Get the specified tournament
    :param request: The incoming request
    :param tournament_id: The tournament's ID
    """
    tournament = get_object_or_404(Tournoi, pk=tournament_id)
    return render(request, 'tournaments/tournoi_detail.html', context_with_user(request,{'tournoi': tournament}))

def pouleDetail(request, pool_id):
    """
    Get the specified pool
    :param request: The incoming request
    :param tournament_id: The pool's ID
    """
    pool = get_object_or_404(Poule, pk=pool_id)
    return render(request, 'tournaments/poule_detail.html', context_with_user(request,{'poule': pool}))

def matchDetail(request, match_id, comment_id = None):
    """
    Get the details of the specified match. If a POST request is submitted, it creates a comment or edits the one
    specified by comment_id.
    :param request: The incoming request
    :param match_id: The match's ID
    :param comment_id: The comment to edit's ID. If None, we display a form to create a new comment.
    """
    match = get_object_or_404(Match, pk=match_id)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            if comment_id:
                comment = Commentaire.objects.get(pk=comment_id)
            else :
                comment = Commentaire.objects.create(
                author = request.user,
                match = match,
                date_time = timezone.now())
            comment.content = form.cleaned_data['content']
            comment.save()
            form = CommentForm()

            if comment_id:
                #if we edited a comment, we want to go back to the basic match_detail url
                return redirect("tournaments:match_detail", match_id= match_id)
    else :
        if comment_id :
            if request.user.is_authenticated:
                form = CommentForm(instance=Commentaire.objects.get(pk=comment_id))
            else :
                form = None
        else :
            if request.user.is_authenticated:
                form = CommentForm()
            else :
                form = None
                
    return render(request, 'tournaments/match_detail.html', context_with_user(request,{'match': match, 'form':form, 'comment_id':comment_id}))

    
        