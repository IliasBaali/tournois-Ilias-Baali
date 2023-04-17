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
    
    
class Player(models.Model):
    name = models.CharField(max_length=200)
    team = models.ForeignKey(Team, verbose_name=("Team"), on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name
    
