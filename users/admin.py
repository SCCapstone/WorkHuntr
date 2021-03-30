from django.contrib import admin
from .models import Comment, Profile, Skill, History

admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Skill)
admin.site.register(History)