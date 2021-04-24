#
# Admin page configuration for Users
#

from django.contrib import admin
from .models import Comment, Profile, Skill, History

# Register the Profile model on the Admin page
admin.site.register(Profile)
# Register the Comment model on the Admin page
admin.site.register(Comment)
# Register the Skill model on the Admin page
admin.site.register(Skill)
# Register the History model on the Admin page
admin.site.register(History)
