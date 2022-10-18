from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import club
from .serializers import ClubListSerializer
from users.serializers import ClubUserSerializer

@api_view(['GET', 'POST'])
def club_list(request):
    if request.method == 'GET':
        clubs = club.objects.all()
        serializer = ClubUserSerializer(clubs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ClubListSerializer(data = request.data)
        if serializer.is_valid(raise_exception= True):
            serializer.save()
            return Response(serializer.data)

