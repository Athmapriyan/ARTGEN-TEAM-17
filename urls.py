from django.urls import path
from .views import submit_code, leaderboard

urlpatterns = [
    path('submit/', submit_code),
    path('leaderboard/', leaderboard),
]
