from rest_framework import serializers
from bgdtapi.models import BGDTUser
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class BGDTUserSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(read_only=True)
    class Meta:
        model = BGDTUser
        fields = ('id', 'bio', 'profile_image_url', 'user_Id')