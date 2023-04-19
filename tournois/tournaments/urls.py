from django.urls import path

from . import views

app_name = 'tournaments'
urlpatterns = [
    path('', views.tournois, name='tournois'),
    path('tournoi/<int:tournament_id>/', views.tournoiDetail, name="tournoi_detail"),
    path('poule/<int:pool_id>/', views.pouleDetail, name="poule_detail"),
    path('match/<int:match_id>/', views.matchDetail, name="match_detail"),
]

