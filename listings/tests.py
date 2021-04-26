from django.test import TestCase
import datetime
from django.contrib.auth.models import User
from .models import Listings,Update



# A function called to test the functionality of the Listings database. It creates a copy of the DB, fills in the values
# and check to ensure that te values were set correctly. the copy is then later destroyed.
class TestListing(TestCase):
    # sets up the temp listing to go into the database
    def setUp(self):
        self.user = User.objects.create_user(username='tester', email='tester@...', password='test123')
        self.user2 = User.objects.create_user(username='tester2', email='tester@...', password='test123')
        self.listing = Listings.objects.create(title='test', date=datetime.datetime.now(), price=1.0, description='this is a test',
                                status='test', tag_one='AI', tag_two='Java', tag_three='Python', huntee=self.user,
                                hunter=self.user2)

    # All the functions below work the same way: pull the listing from the temp database, grab the field of whichever
    # Value is to be tested, actually grab the value from the field, and then run an assertion from the value against
    # What I as the test writer knows the value should be. Finally, print that the test passed (which is mostly for
    # debugging purposes)

    # Tests the huntee value in the Listing database
    def test_Huntee(self):
        listing = Listings.objects.get(id=1)
        field_object = Listings._meta.get_field('huntee')
        value = field_object.value_from_object(listing)
        self.assertEqual(value, self.user.id)
        print("Huntee PASS")

    # Tests the hunter value in the Listing database
    def test_Hunter(self):
        listing = Listings.objects.get(id=1)
        field_object = Listings._meta.get_field('hunter')
        value = field_object.value_from_object(listing)
        self.assertEqual(value, self.user2.id)
        print("Hunter PASS")

    # Tests the Title value in the Listing database
    def test_Title(self):
        listing = Listings.objects.get(id=1)
        field_object = Listings._meta.get_field('title')
        value = field_object.value_from_object(listing)
        self.assertEqual(value, 'test')
        print("Title PASS")

    # Tests the Price value in the Listing database
    def test_Price(self):
        listing = Listings.objects.get(id=1)
        field_object = Listings._meta.get_field('price')
        value = field_object.value_from_object(listing)
        self.assertEqual(value, 1.0)
        print("Price PASS")

    # Tests the description value in the Listing database
    def test_Description(self):
        listing = Listings.objects.get(id=1)
        field_object = Listings._meta.get_field('description')
        value = field_object.value_from_object(listing)
        self.assertEqual(value, 'this is a test')
        print("Description PASS")

    def test_Date(self):
        listing = Listings.objects.get(id=1)
        field_object = Update._meta.get_field('date')
        value = field_object.value_from_object(listing)
        self.assertEqual(value, self.listing.date)
        print("Listing Date PASS")

    # Tests the Status value in the Listing database
    def test_Status(self):
        listing = Listings.objects.get(id=1)
        field_object = Listings._meta.get_field('status')
        value = field_object.value_from_object(listing)
        self.assertEqual(value, 'test')
        print("Status PASS")

    # Tests all 3 of the tags in the Listing database. 3 separate tests for the same thing was redundant.
    def test_Tags(self):
        listing = Listings.objects.get(id=1)
        field_object = Listings._meta.get_field('tag_one')
        value = field_object.value_from_object(listing)
        field_object = Listings._meta.get_field('tag_two')
        value2 = field_object.value_from_object(listing)
        field_object = Listings._meta.get_field('tag_three')
        value3 = field_object.value_from_object(listing)
        self.assertEqual(value, 'AI')
        self.assertEqual(value2, 'Java')
        self.assertEqual(value3, 'Python')
        print("Tags PASS")

    # Deletes the user after ever test call to prevent unique errors in the DB
    def tearDown(self):
        self.user.delete()


class TestListingUpdate(TestCase):
    # sets up the temp listing to go into the database
    def setUp(self):
        self.user = User.objects.create_user(username='tester', email='tester@...', password='test123')
        self.user2 = User.objects.create_user(username='tester2', email='tester@...', password='test123')
        self.listing = Listings.objects.create(title='test', date=datetime.datetime.now(), price=1.0, description='this is a test',
                                status='test', tag_one='AI', tag_two='Java', tag_three='Python', huntee=self.user,
                                hunter=self.user2)
        self.Update = Update.objects.create(date=datetime.datetime.now(), status="testSta", description="testDes",
                                            listing=self.listing)

    # Tests the Status value in the UpdateListing database
    def test_Status(self):
        update = Update.objects.get(id=1)
        field_object = Update._meta.get_field('status')
        value = field_object.value_from_object(update)
        self.assertEqual(value, 'testSta')
        print("Update Status PASS")

    # Tests the date value in the UpdateListing database
    def test_Date(self):
        update = Update.objects.get(id=1)
        field_object = Update._meta.get_field('date')
        value = field_object.value_from_object(update)
        self.assertEqual(value, self.Update.date)
        print("Update Date PASS")

    # Tests the Status value in the UpdateListing database
    def test_Description(self):
        update = Update.objects.get(id=1)
        field_object = Update._meta.get_field('description')
        value = field_object.value_from_object(update)
        self.assertEqual(value, 'testDes')
        print("Update Description PASS")

    # Tests the Status value in the UpdateListing database
    def test_Listing(self):
        update = Update.objects.get(id=1)
        field_object = Update._meta.get_field('listing')
        value = field_object.value_from_object(update)
        self.assertEqual(value, self.listing.id)
        print("Update Listing PASS")

    # Deletes the update after ever test call to prevent unique errors in the DB
    def tearDown(self):
        self.Update.delete()