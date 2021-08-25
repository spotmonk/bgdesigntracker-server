from django.db import models
from django.db.models.deletion import CASCADE

class Game(models.Model):
    name = models.CharField(max_length=400)
    creationDate = models.DateField(auto_now_add=True)
    description = models.TextField()
    imageUrl = models.TextField(max_length=200)
    userId = models.ForeignKey("BGDTUser",
        on_delete=CASCADE,
        related_name="usergames",
        related_query_name="usergame")