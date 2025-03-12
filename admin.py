from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Problem)
admin.site.register(Submission)
admin.site.register(Leaderboard)
admin.site.register(Contest)
admin.site.register(LiveContest)
admin.site.register(UserRating)
admin.site.register(Discussion)
admin.site.register(Achievement)
admin.site.register(ProblemFeedback)
