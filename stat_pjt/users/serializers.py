from rest_framework import serializers
from .models import User
from clubs.serializers import ClubListSerializer
from clubs.models import club

class UserListSerializer(serializers.ModelSerializer):
    clubs = ClubListSerializer(many=True, read_only = True)
    class Meta:
        model = User
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class ClubUserSerializer(serializers.ModelSerializer):
    users = UserSerializer(many= True, read_only = True)
    class Meta:
        model = club
        fields = '__all__'
