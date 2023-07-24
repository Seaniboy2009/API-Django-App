from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

# Function view
def profiles(request):
    return HttpResponse("Hello World")
