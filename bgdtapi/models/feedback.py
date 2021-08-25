from django.db import models
from django.db.models.deletion import CASCADE


class Feedback(models.Model):
    playerName = models.CharField(max_length=200)
    goodStuff = models.TextField()
    badStuff = models.TextField()
    favoriteFeature = models.TextField()
    enjoyment = models.IntegerField()
    playAgain = models.BooleanField()
    playtestNumber = models.IntegerField()
    playtestId = models.ForeignKey("Playtest",
        on_delete=CASCADE,
        related_name="playtestFeedbacks",
        related_query_name="playtestFeedback")
