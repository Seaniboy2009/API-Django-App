from django.urls import path
from . import views

# Function URLS
urlpatterns = [
    # Function URL
    # path('profiles/', views.profiles, name='profiles'),
    path('entrys/', views.EntrysList.as_view()),
]