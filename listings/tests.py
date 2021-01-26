from django.test import TestCase
import datetime
from django.contrib.auth.models import User
from .models import Listings


class TestListing(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='tester', email='tester@...', password='test123')
        Listings.objects.create(title='test', date=datetime.datetime.now(), price=1.0, description='this is a test',
                                status='test', tag1='test1', tag2='test2', tag3='test3', huntee=self.user,
                                hunter=self.user)

    def test_Title(self):
        listing = Listings.objects.get(id=1)
        field_object = Listings._meta.get_field('title')
        value = field_object.value_from_object(listing)
        self.assertEqual(value, 'test')
