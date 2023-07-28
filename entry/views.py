from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Entry
from .serializers import EntrySerializer

class EntrysList(generics.ListAPIView):

    # This gets the serialiser information to display 
    serializer_class = EntrySerializer

    queryset = Entry.objects.all()

