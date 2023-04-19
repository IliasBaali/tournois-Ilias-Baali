from django.db import models

# Create your models here.

class Tournoi(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, null=True)
    start_date = models.DateTimeField("Start date", null = True)
    end_date = models.DateTimeField("End date", null = True)
    nb_pools = models.IntegerField("Number of pools")
    nb_teams_in_pool = models.IntegerField("Number of teams per pool")
    
    def __str__(self) -> str:
        return self.name
    
class Team(models.Model):
    name = models.CharField("Name of the team", max_length=200)
    coach_name = models.CharField("Name of the coach", max_length=200)
    def __str__(self) -> str:
        return self.name
    
class Poule(models.Model):
    pool_number = models.IntegerField("Pool number")
    tournament = models.ForeignKey("Tournoi", verbose_name=("Tournament"), on_delete=models.CASCADE)
    teams = models.ManyToManyField(Team)   
    def __str__(self) -> str:
        return "Pool " + str(self.pool_number) + ", " + str(self.tournament)
    #TODO: liste des matchs, calcul du classement
    
class Player(models.Model):
    name = models.CharField(max_length=200)
    team = models.ForeignKey(Team, verbose_name=("Team"), on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name
    
class Match(models.Model):
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
    
    
class Commentaire(models.Model):
    author = models.CharField(max_length=200)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    date_time = models.DateTimeField('Publication date', auto_now=False, auto_now_add=False)
    content = models.CharField(max_length=500)
    def __str__(self) -> str:
        return self.content