from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Message
from .signals import message_read, message_sent

class MessagingService(object):
    
    def send_message(self, sender, recipient, message):
        if sender == recipient:
            raise ValidationError("You can't send messages to yourself.")
        message = Message(sender=sender, recipient=recipient, content=str(message))
        message.save()
        message_sent.send(sender=message, from_user=message.sender, to_user=message.recipient)
        return message, 200

    def get_unread_messages(self, user):
        return Message.objects.all().filter(recipient=user, read_at=None)

    def read_message(self, message_id):
        try:
            message = Message.objects.get(id=message_id)
            self.mark_as_read(message)
            return message.content
        except Message.DoesNotExist:
            return ""

    def read_message_formatted(self, message_id):
        try:
            message = Message.objects.get(id=message_id)
            self.mark_as_read(message)
            return message.sender.username + ": " + message.content
        except Message.DoesNotExist:
            return ""
    
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

    def mark_as_read(self, message):
        if message.read_at is None:
            message.read_at = timezone.now()
            message_read.send(sender=message, from_user=message.sender, to=message.recipient)
            message.save()
