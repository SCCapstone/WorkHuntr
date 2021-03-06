#
# Models for the Dms app
#

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

#
# Model for direct messages between users
#
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='sender')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='receiver')
    content = models.TextField(_("Content"))
    sent_at = models.DateTimeField(_("sent at"), null=True, blank=True)
    read_at = models.DateTimeField(_("read at"), null=True, blank=True)

    # A message is unread if it has no read_at
    @property
    def unread(self):
        if self.read_at is not None:
            return False
        return True

    # String representation of the Message model
    def __str__(self):
        return self.content

    # Save a message to the database
    def save(self, **kwargs):
        if self.sender == self.recipient:
            raise ValidationError("You can't send messages to yourself!")
        if not self.id:
            self.sent_at = timezone.now()
        super(Message, self).save(**kwargs)
