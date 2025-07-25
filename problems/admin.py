from django.contrib import admin
from .models import CodeforcesContest,LeetcodeContest
from .models import UserProfile
admin.site.register(CodeforcesContest)
admin.site.register(LeetcodeContest)
admin.site.register(UserProfile)
# Register your models here.
