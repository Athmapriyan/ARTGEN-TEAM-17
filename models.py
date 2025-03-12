from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now

class CustomUser(AbstractUser):
    ROLE_CHOICES = (('admin', 'Admin'), ('participant', 'Participant'), ('judge', 'Judge'))
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='participant')

class Problem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    test_cases = models.JSONField()
    time_limit = models.FloatField(default=2.0)
    memory_limit = models.IntegerField(default=256)

class Submission(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    code = models.TextField()
    language = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default='Pending')
    score = models.IntegerField(default=0)
    submission_time = models.DateTimeField(default=now)

class Leaderboard(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

class Contest(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    problems = models.ManyToManyField(Problem)

class LiveContest(models.Model):
    contest = models.OneToOneField(Contest, on_delete=models.CASCADE)
    duration = models.IntegerField()
    active = models.BooleanField(default=True)

class UserRating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1200)

class Discussion(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Achievement(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    earned_date = models.DateTimeField(auto_now_add=True)

class ProblemFeedback(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    difficulty = models.IntegerField()
