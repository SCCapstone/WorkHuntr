#
# Admin page configuration for Message
#

from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ('id', 'sender', 'content')

# Register the Message model on the Admin page
admin.site.register(Message, MessageAdmin)
