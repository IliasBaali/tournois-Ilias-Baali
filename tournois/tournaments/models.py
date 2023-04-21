from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tournoi(models.Model):
    "A tournament"
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, null=True)
    start_date = models.DateTimeField("Start date", null = True)
    end_date = models.DateTimeField("End date", null = True)
    nb_pools = models.IntegerField("Number of pools")
    nb_teams_in_pool = models.IntegerField("Number of teams per pool")
    
    def __str__(self) -> str:
        return self.name
    
class Team(models.Model):
    "A team, that can take part in multiple tournament"
    name = models.CharField("Name of the team", max_length=200)
    coach_name = models.CharField("Name of the coach", max_length=200)
    
    def __str__(self) -> str:
        return self.name
    
    
class Poule(models.Model):
    "A pool of a specific tournament, that contains teams"
    pool_number = models.IntegerField("Pool number")
    tournament = models.ForeignKey("Tournoi", verbose_name=("Tournament"), on_delete=models.CASCADE)
    teams = models.ManyToManyField(Team)   
    def __str__(self) -> str:
        return "Poule " + str(self.pool_number) + ", " + str(self.tournament)
    #TODO: liste des matchs, calcul du classement
    def get_score_list(self):
        score_list = []
        for team in self.teams:
            score_list[team.name] = 0
        for match in self.match_set.all():
            winner = match.get_winner()
            if winner :
                score_list[winner.name] += 1
        return score_list
            
    
class Player(models.Model):
    "A player, member of a team (not used for the moment)"
    name = models.CharField(max_length=200)
    team = models.ForeignKey(Team, verbose_name=("Team"), on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name
    
class Match(models.Model):
    "A match, that opposes two teams"
    date = models.DateField("Date of the match")
    time = models.TimeField("Time of the match")
    location = models.CharField(max_length=200)
    team_1 = models.ForeignKey(Team, verbose_name=("Team 1"), on_delete=models.CASCADE, related_name="team_1")
    team_2 = models.ForeignKey(Team, verbose_name=("Team 2"), on_delete=models.CASCADE, related_name="team_2")
    score_1 = models.IntegerField("Score of team 1", blank=True, null=True)
    score_2 = models.IntegerField("Score of team 2", blank=True, null=True)
    pool = models.ForeignKey(Poule, verbose_name=("Pool"), on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str(self.team_1) + " VS " + str(self.team_2)
    
    def get_winner(self):
        if not self.score_1 or not self.score_2:
            return None
        if self.score_1 >= self.score_2:
            return self.team_1
        if self.score_2 >= self.score_1:
            return self.team_2
    
    
class Commentaire(models.Model):
    "A comment about a match, posted by an authenticated author"
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    date_time = models.DateTimeField('Publication date', auto_now=False, auto_now_add=False)
    content = models.CharField(max_length=500)
    def __str__(self) -> str:
        return self.content