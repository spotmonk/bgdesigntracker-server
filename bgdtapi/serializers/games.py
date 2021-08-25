from rest_framework import serializers
from bgdtapi.models import Game

class Gameerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Game
        fields = ('id', "name", "creationDate", "description", "imageUrl", "userId")