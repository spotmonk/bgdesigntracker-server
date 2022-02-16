from django.db import models
from django.db.models.deletion import CASCADE


class Playtest(models.Model):
    Location = models.CharField(max_length=100)
    badNotes = models.TextField()
    goodNotes = models.TextField()
    generalNotes = models.TextField()
    playDateTime = models.DateTimeField()
    playerCount = models.IntegerField()
    playtestFeel = models.IntegerField()
    playtestGoals = models.TextField()
    playtestType = models.CharField(max_length=100)
    versionId = models.ForeignKey("Version",
        on_delete=CASCADE,
        related_name="versionPlaytests",
        related_query_name="versionPlaytest")