#
# Models for the Users app
#

from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.urls import reverse
from PIL import Image
import random

# Model for a 2FA code
class Code(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=5, blank=True)

    # String representation of a Code
    def __str__(self):
        return str(self.number)
    
    # Save a Code
    def save(self):
        super().save()
        number_list = [x for x in range(0, 10)]
        code_items = []
        for i in range(0, 5):
            num = random.choice(number_list)
            code_items.append(num)
        code_string = "".join(str(item) for item in code_items)
        self.number = code_string

#
# Model for a User Profile
#
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(default='Other', max_length=5)
    phone_number = models.CharField(max_length=12)
    gender = models.CharField(default='Prefer Not to Say', max_length=20)
    birthday = models.CharField(default='XXXX-XX-XX', max_length=10)
    current_employment = models.CharField(default='No Employment', max_length=20)
    account_type = models.CharField(default='Huntee', max_length=6)
    profile_picture = CloudinaryField('Profile picture', default='default/default.jpg')
    resume = CloudinaryField('Resume (.pdf only)', validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True, blank=True)
    website = models.URLField(default='', max_length=200, blank=True)
    privacy = models.CharField(default='Public', max_length=10)
    has_unread_messages = models.BooleanField(default=False)
    
    # String representation of a Profile
    def __str__(self):
        return f'{self.user.username} Profile'

    # Save a Profile
    #def save(self):
        #super().save()
        #img = Image.open(self.profile_picture.path)
        #if img.height > 300 or img.width > 300:
            #output_size = (300, 300)
            #img.thumbnail(output_size)
            #img.save(self.profile_picture.path)

#
# Model for a Comment on a Profile
#
class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    comment = models.CharField(default='', max_length=500)
    rating = models.CharField(default='1', max_length=1)
    company = models.CharField(default='', max_length=20)

    # String representation of a Comment
    def __str__(self):
        return self.comment, self.rating, self.company

#
# Model for a Skill on a Profile
#
class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    skill = models.CharField(default='', max_length=20)

    # String representation of a Skill
    def __str__(self):
        return self.skill

#
# Model for a History on a Profile
#
class History(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    company = models.CharField(default='', max_length=20)
    description = models.CharField(default='', max_length=500)
    start_date = models.CharField(default='XX/XX/XXXX', max_length=10)
    end_date = models.CharField(default='XX/XX/XXXX', max_length=10)

    # String representation of a History
    def __str__(self):
        return self.company, self.description, self.start_date, self.end_date
