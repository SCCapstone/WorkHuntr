from django.test import TestCase
import datetime
from django.contrib.auth.models import User
from .models import Message
import pytz
from django.db import models
from django.utils import timezone


# A function called to test the functionality of the Message database. It creates a copy of the DB, fills in the values
# and check to ensure that te values were set correctly. the copy is then later destroyed.
class TestListing(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='sender', email='sender@...', password='test123')
        self.user2 = User.objects.create_user(username='receiver', email='reveiver@...', password='test123')
        self.message = Message.objects.create(sender=self.user, recipient=self.user2, content='testMSG',
                               sent_at=datetime.datetime.now(),
                               read_at=pytz.utc.localize(datetime.datetime.strptime('2007-10-25 14:30:59', '%Y-%m-%d %H:%M:%S')))

    # Tests the content field of the message
    def test_content(self):
        message = Message.objects.get(id=1)
        field_object = Message._meta.get_field('content')
        value = field_object.value_from_object(message)
        self.assertEqual(value, 'testMSG')
        print("content PASS")

    # Tests the sent_at field of the message
    def test_Sent_At(self):
        message = Message.objects.get(id=1)
        field_object = Message._meta.get_field('sent_at')
        value = field_object.value_from_object(message)
        self.assertEqual(value, self.message.sent_at)
        print("Sent_At PASS")

    # Tests the read_at field of the message
    def test_Read_At(self):
        message = Message.objects.get(id=1)
        field_object = Message._meta.get_field('read_at')
        value = field_object.value_from_object(message)
        self.assertEqual(value, pytz.utc.localize(datetime.datetime.strptime('2007-10-25 14:30:59', '%Y-%m-%d %H:%M:%S', )))
        print("Read_At PASS")

    # Tests the read_at field of the message
    def test_Sender(self):
        message = Message.objects.get(id=1)
        field_object = Message._meta.get_field('sender')
        value = field_object.value_from_object(message)
        self.assertEqual(value, self.user.id)
        print("Sender PASS")

    # Tests the recipient field of the message
    def test_Recipient(self):
        message = Message.objects.get(id=1)
        field_object = Message._meta.get_field('recipient')
        value = field_object.value_from_object(message)
        self.assertEqual(value, self.user2.id)
        print("Recipient PASS")
