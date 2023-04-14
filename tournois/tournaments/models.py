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
    
