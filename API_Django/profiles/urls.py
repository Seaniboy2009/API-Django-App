from django.urls import path
from . import views

# Function URLS
urlpatterns = [
    path('profiles/', views.profiles, name='profiles')
]