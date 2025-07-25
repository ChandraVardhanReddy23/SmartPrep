from django.db import models
from django.contrib.auth.models import User
class CodeforcesContest(models.Model):
    handle = models.CharField(max_length=100)
    contest_name = models.CharField(max_length=255)
    rank = models.IntegerField()
    old_rating = models.IntegerField()
    new_rating = models.IntegerField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.handle} — {self.contest_name}"

class LeetcodeContest(models.Model):
    handle = models.CharField(max_length=100)
    attended_contests = models.IntegerField()
    rating = models.FloatField()
    global_ranking = models.IntegerField()
    total_participants = models.IntegerField()
    top_percentage = models.FloatField()

    def __str__(self):
        return f"{self.handle} — {self.rating}"

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    codeforces_handle = models.CharField(max_length=100, blank=True)
    leetcode_handle = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
