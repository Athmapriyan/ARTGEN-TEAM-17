import os
import subprocess
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now

# Ensure Django settings are properly configured before importing Django modules
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")  # Replace 'myproject' with your project name
django.setup()

# task 1 implement user authentication in different level

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('participant', 'Participant'),
        ('judge', 'Judge'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='participant')

# task 2 create a Problem Submission System
class Problem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    test_cases = models.JSONField()
  
class Submission(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    code = models.TextField()
    status = models.CharField(max_length=50, default='Pending')
    score = models.IntegerField(default=0)
    submission_time = models.DateTimeField(default=now)

#task 3 devolop real time leader board

class Leaderboard(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
  
# task 4 Code Execution Sandbox

SUPPORTED_LANGUAGES = {
    'python': 'python3',
    'cpp': 'g++',
    'java': 'javac'
}

