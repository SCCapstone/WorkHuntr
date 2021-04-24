#
# Messaging service to handle direct messages between users
#

from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Message
from .signals import message_read, message_sent

class MessagingService(object):
    
    # Send a message from a user to a user
    def send_message(self, sender, recipient, message):
        if sender == recipient:
            raise ValidationError("You can't send messages to yourself.")
        message = Message(sender=sender, recipient=recipient, content=str(message))
        message.save()
        message_sent.send(sender=message, from_user=message.sender, to_user=message.recipient)
        return message, 200

    # Get all unread messages for a user
    def get_unread_messages(self, user):
        return Message.objects.all().filter(recipient=user, read_at=None)

    # Read the contents of a message
    def read_message(self, message_id):
        try:
            message = Message.objects.get(id=message_id)
            self.mark_as_read(message)
            return message.content
        except Message.DoesNotExist:
            return ""

    # Get the messages between two users
    def get_conversations(self, user1, user2, limit=None, reversed=False, mark_read=False):
        users = [user1, user2]
        if reversed:
            order = '-pk'
        else:
            order = 'pk'
        conversation = Message.objects.all().filter(sender=user1, recipient=user2).order_by(order)
        if limit:
            conversation = conversation[:limit]
        if mark_read:
            for message in conversation:
                self.mark_as_read(message)
        return conversation

    # Mark a message as read
    def mark_as_read(self, message):
        if message.read_at is None:
            message.read_at = timezone.now()
            message_read.send(sender=message, from_user=message.sender, to=message.recipient)
            message.save()
