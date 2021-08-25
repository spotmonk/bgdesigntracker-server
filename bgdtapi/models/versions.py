from django.db import models
from django.db.models.deletion import CASCADE


class Version(models.Model):
    versionNumber = models.CharField(max_length=100)
    creationDate = models.DateField(auto_now_add=True)
    changes = models.TextField()
    imageUrl = models.TextField(max_length=200)
    gameId = models.ForeignKey("Game",
        on_delete=CASCADE,
        related_name="gameversions",
        related_query_name="gamesversion")