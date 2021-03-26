
from django.test import TestCase
import datetime
from django.contrib.auth.models import User
from .models import Listings

class TestListing(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', email='tester@...', password='test123')
        self.user2 = User.objects.create_user(username='tester2', email='tester@...', password='test123')
        Listings.objects.create(title='test', date=datetime.datetime.now(), price=1.0, description='this is a test',
                                status='test', tag1='test1', tag2='test2', tag3='test3', huntee=self.user,
                                hunter=self.user2)
    def test_Huntee(self):
        listing = Listings.objects.get(id=1)
        field_object = Listings._meta.get_field('huntee')
        value = field_object.value_from_object(listing)
        self.assertEqual(value, self.user.id)
        print("Huntee PASS")

    def test_Hunter(self):
        listing = Listings.objects.get(id=1)
        field_object = Listings._meta.get_field('hunter')
        value = field_object.value_from_object(listing)
        self.assertEqual(value, self.user2.id)
        print("Hunter PASS")

    def test_Title(self):
        listing = Listings.objects.get(id=1)
        field_object = Listings._meta.get_field('title')
        value = field_object.value_from_object(listing)
        self.assertEqual(value, 'test')
        print("Title PASS")


    def test_Price(self):
        listing = Listings.objects.get(id=1)
        field_object = Listings._meta.get_field('price')
        value = field_object.value_from_object(listing)
        self.assertEqual(value, 1.0)
        print("Price PASS")

    def test_Description(self):
        listing = Listings.objects.get(id=1)
        field_object = Listings._meta.get_field('description')
        value = field_object.value_from_object(listing)
        self.assertEqual(value, 'this is a test')
        print("Description PASS")

    def test_Status(self):
        listing = Listings.objects.get(id=1)
        field_object = Listings._meta.get_field('status')
        value = field_object.value_from_object(listing)
        self.assertEqual(value, 'test')
        print("Status PASS")

    def test_Tags(self):
        listing = Listings.objects.get(id=1)
        field_object = Listings._meta.get_field('tag1')
        value = field_object.value_from_object(listing)
        field_object = Listings._meta.get_field('tag2')
        value2 = field_object.value_from_object(listing)
        field_object = Listings._meta.get_field('tag3')
        value3 = field_object.value_from_object(listing)
        self.assertEqual(value, 'test1')
        self.assertEqual(value2, 'test2')
        self.assertEqual(value3, 'test3')
        print("Tags PASS")

    def tearDown(self):
        self.user.delete()