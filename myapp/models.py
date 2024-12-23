from django.db import models

# Create your models here.
class Header(models.Model):
    header_title1 = models.CharField(max_length=50)
    header_title2 = models.CharField(max_length=50)
    header_title3 = models.CharField(max_length=50)
    header_image = models.FileField(upload_to='image/')
    
    
class Tournament(models.Model):
    Tournaments_prize = models.CharField(max_length=50)
    Tournaments_detail = models.CharField(max_length=50)
    Tournaments_image = models.FileField(upload_to='image/')
    
class TeamMember(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name (Govt ID Proof)")
    game_name = models.CharField(max_length=50)
    unique_game_id = models.CharField(max_length=50)
    team_id = models.IntegerField()  # To group members of a team

    def __str__(self):
        return self.name



class Winner(models.Model):
    winner_team_image = models.FileField(upload_to='image/')
    winner_team_played = models.CharField(max_length=50)
    winner_team_mode = models.CharField(max_length=50)
    winner_team_name = models.CharField(max_length=50)
    winner_team_game_win = models.CharField(max_length=50)