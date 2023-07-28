from django.urls import path
from . import views

# Function URLS
urlpatterns = [
    # Function URL
    # path('profiles/', views.profiles, name='profiles'),
    path('entries/', views.EntriesList.as_view()),
]