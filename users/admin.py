from django.contrib import admin
from .models import Profile, Comment

admin.site.register(Profile)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'comment', 'active')
    list_filter = ('active',)
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)