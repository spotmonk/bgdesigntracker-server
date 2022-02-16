from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE

class BGDTUser(models.Model):
    bio = models.TextField()
    profile_image_url = models.CharField(max_length=200)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)