from rest_framework import serializers
from .models import club
#from users.serializers import UserListSerializer


class ClubListSerializer(serializers.ModelSerializer):
    #users = UserListSerializer(many=True)
    class Meta:
        model = club
        fields = '__all__'
