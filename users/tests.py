"""from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(id=123, username='TestUser', email='tester2@...', password='test123')
        Profile.objects.create(user_id=123, phone_number="1234567890", title='TestTit', gender='TestGen', birthday="08221999",
                               current_employment="TestEmp", account_type='TestTyp', website='Test.com',
                               privacy='TestPri')

    def test_PhoneNumber(self):
        profile = Profile.objects.get(id=1)
        field_object = Profile._meta.get_field('phone_number')
        value = field_object.value_from_object(profile)
        self.assertEqual(value, '1234567890')
        print("Phone_Number PASS")

    def test_Title(self):
        profile = Profile.objects.get(id=1)
        field_object = Profile._meta.get_field('title')
        value = field_object.value_from_object(profile)
        self.assertEqual(value, 'TestTit')
        print("Title PASS")

    def test_Gender(self):
        profile = Profile.objects.get(id=1)
        field_object = Profile._meta.get_field('gender')
        value = field_object.value_from_object(profile)
        self.assertEqual(value, 'TestGen')
        print("Gender PASS")

    def test_Birthday(self):
        profile = Profile.objects.get(id=1)
        field_object = Profile._meta.get_field('birthday')
        value = field_object.value_from_object(profile)
        self.assertEqual(value, '08221999')
        print("Birthday PASS")

    def test_Current_Employment(self):
        profile = Profile.objects.get(id=1)
        field_object = Profile._meta.get_field('current_employment')
        value = field_object.value_from_object(profile)
        self.assertEqual(value, 'TestEmp')
        print("Current_Employment PASS")

    def test_Account_Type(self):
        profile = Profile.objects.get(id=1)
        field_object = Profile._meta.get_field('account_type')
        value = field_object.value_from_object(profile)
        self.assertEqual(value, 'TestTyp')
        print("Account_Type PASS")

    def test_Website(self):
        profile = Profile.objects.get(id=1)
        field_object = Profile._meta.get_field('website')
        value = field_object.value_from_object(profile)
        self.assertEqual(value, 'Test.com')
        print("Website PASS")

    def test_Title(self):
        profile = Profile.objects.get(id=1)
        field_object = Profile._meta.get_field('username')
        value = field_object.value_from_object(profile)
        self.assertEqual(value, 'TestUse')
        print("Username PASS")

    def test_Privacy(self):
        profile = Profile.objects.get(id=1)
        field_object = Profile._meta.get_field('Privacy')
        value = field_object.value_from_object(profile)
        self.assertEqual(value, 'TestPri')
        print("Privacy PASS")
"""