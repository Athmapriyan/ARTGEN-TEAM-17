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

def execute_code(code, language):
    filename = f'temp_code.{language}'
    with open(filename, 'w') as f:
        f.write(code)
    try:
        result = subprocess.run([SUPPORTED_LANGUAGES.get(language, 'python3'), filename], capture_output=True, text=True, timeout=5)
        return result.stdout
    except subprocess.TimeoutExpired:
        return "Execution Timed Out"

# task 5 Plagiarism Detection 

def check_plagiarism(submissions):
    code_texts = [sub.code for sub in submissions]
    return len(set(code_texts)) != len(code_texts)

# task 6 Contest Scheduling

class Contest(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    problems = models.ManyToManyField(Problem)

# task 7 Rating System

class UserRating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1200)

# task 8 live coding competition

class LiveContest(models.Model):
    contest = models.OneToOneField(Contest, on_delete=models.CASCADE)
    duration = models.IntegerField()
    active = models.BooleanField(default=True)

# task 9 Multi-Language Support (Handled in Sandbox Execution)
class LanguageSupport(models.Model):
    language = models.CharField(max_length=50)
    compiler = models.CharField(max_length=255)

# task 10 Group Contests
class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(CustomUser)

# task 11 API for External Evaluation (Using Django Rest Framework)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CodeEvaluationAPI(APIView):
    def post(self, request):
        code = request.data.get("code")
        language = request.data.get("language")
        output = execute_code(code, language)
        return Response({"output": output}, status=status.HTTP_200_OK)

# task 12 Admin Panel (Django Admin Customization)
from django.contrib import admin

admin.site.register(CustomUser)
admin.site.register(Problem)
admin.site.register(Contest)
admin.site.register(Leaderboard)
admin.site.register(Submission)

# task 13 Problem Recommendation System (Using Past Data Analysis)
class ProblemRecommendation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    recommended_problems = models.ManyToManyField(Problem)

# task 14 Achievements & Badges
class Achievement(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_earned = models.DateTimeField(auto_now_add=True)

# task 15 Automated Test Case Generator (Basic Implementation)
def generate_test_cases():
    return [{'input': '2\n3 4', 'output': '7'}, {'input': '5\n6 7', 'output': '13'}]

# task 16 Submission History Tracker
class SubmissionHistory(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    verdict = models.CharField(max_length=50)

# task 17 Discussion Forum
class Discussion(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# task 18 Problem Difficulty Rating
class ProblemDifficulty(models.Model):
    problem = models.OneToOneField(Problem, on_delete=models.CASCADE)
    difficulty = models.FloatField(default=0.0)

# task 19 Secure Backup & Recovery
def backup_data():
    os.system('pg_dump mydatabase > backup.sql')

def restore_data():
    os.system('psql mydatabase < backup.sql')

# task 20 Analytics Dashboard (Basic Model)
class Analytics(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    total_submissions = models.IntegerField()
    average_score = models.FloatField()
    top_performer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)




    
