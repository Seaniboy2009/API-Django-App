from django.shortcuts import render
from django.http import HttpResponse

# Function view
def profiles(request):
    return HttpResponse("Hello World")
