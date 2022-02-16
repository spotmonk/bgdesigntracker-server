from rest_framework import serializers
from bgdtapi.models import Image

class ImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Image
        fields = ('id', "image_file")