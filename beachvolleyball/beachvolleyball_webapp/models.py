from django.db import models

# Create your models here.

#Hier werden die Datenbanken erstellt
#Klassen sind die Tabellen

class Event(models.Model):

    Code = models.CharField(null=True, blank=True)
    Name = models.CharField(null=True, blank=True)
    StartDate = models.DateField(null=True, blank=True)
    EndDate = models.DateField(null=True, blank=True)
    no  = models.IntegerField(primary_key=True)
    Version = models.IntegerField(null=True, blank=True)

class BeachTournament(models.Model):

    Code = models.CharField(null=True, blank=True)
    Name = models.CharField(null=True, blank=True)
    StartDateMainDraw = models.DateField(null=True, blank=True)
    EndDateMainDraw = models.DateField(null=True, blank=True)
    FederationCode = models.CharField(null=True, blank=True)
    no = models.IntegerField(primary_key=True)
    Version = models.IntegerField(null=True, blank=True)

class BeachMatch(models.Model):

    NoInTournament = models.IntegerField(null=True, blank=True)
    LocalDate = models.DateField(null=True, blank=True)
    LocalTime = models.TimeField(null=True, blank=True)
    NoTeamA = models.CharField(null=True, blank=True)
    NoTeamB = models.CharField(null=True, blank=True)
    Court = models.CharField(null=True, blank=True)
    MatchPointsA = models.CharField(null=True, blank=True)
    MatchPointsB = models.CharField(null=True, blank=True)
    PointsTeamASet1 = models.CharField(null=True, blank=True)
    PointsTeamBSet1 = models.CharField(null=True, blank=True)
    PointsTeamASet2 = models.CharField(null=True, blank=True)
    PointsTeamBSet2 = models.CharField(null=True, blank=True)
    PointsTeamASet3 = models.CharField(null=True, blank=True)
    PointsTeamBSet3 = models.CharField(null=True, blank=True)
    DurationSet1 = models.CharField(null=True, blank=True)
    DurationSet2 = models.CharField(null=True, blank=True)
    DurationSet3 = models.CharField(null=True, blank=True)
    No = models.CharField(primary_key=True)
    Version = models.CharField(null=True, blank=True)



    
class BeachRound(models.Model):

    Code = models.CharField(null=True, blank=True)
    Name = models.CharField(null=True, blank=True)
    Bracket = models.CharField(null=True, blank=True)
    Phase = models.CharField(null=True, blank=True)
    StartDate = models.DateField(null=True, blank=True)
    EndDate = models.DateField(null=True, blank=True)
    No = models.IntegerField(primary_key=True)
    Version = models.IntegerField(null=True, blank=True)

class BeachTeam(models.Model):

    NoPlayer1 = models.CharField(null=True, blank=True)
    NoPlayer2 = models.CharField(null=True, blank=True)
    Name = models.CharField(null=True, blank=True)
    Rank = models.CharField(null=True, blank=True)
    EarnedPointsTeam = models.CharField(null=True, blank=True)
    EarningsTeam = models.CharField(null=True, blank=True)
    No = models.IntegerField(unique=True)
    Version = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ('No', 'NoPlayer1', 'NoPlayer2')

class Player(models.Model):
    id = models.AutoField(primary_key=True)
    FederationCode = models.CharField(null=True, blank=True)
    FirstName = models.CharField(null=True, blank=True)
    Gender = models.CharField(null=True, blank=True)
    LastName = models.CharField(null=True, blank=True)
    PlaysBeach = models.BooleanField()
    PlaysVolley = models.BooleanField()
    TeamName = models.CharField(null=True, blank=True)
    No = models.IntegerField(null=True, blank=True)
    Version = models.IntegerField(null=True, blank=True)


# Spieler 100001 laut INSIDER INFO gibt es 2 mal (P.S. Simon Says)
# Deswegen unique_together machen und Nationality gibt es auch nicht wurde im Payload entfernt
