from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer

# Function view
# def profiles(request):
#     return HttpResponse("Hello World")


class ProfilesList(generics.ListAPIView):

    # This gets the serialiser information to display 
    serializer_class = ProfileSerializer

    queryset = Profile.objects.all()

