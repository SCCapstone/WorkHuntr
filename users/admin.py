from django.contrib import admin
from .models import Comment, Profile

admin.site.register(Profile)
admin.site.register(Comment)
