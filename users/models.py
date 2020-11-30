from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')

  def __str__(self):
    return f'{self.user.username} Profile'

  def save(self):
    super().save()
    img = Image.open(self.profile_picture.path)
    if img.height > 300 or img.width > 300:
      output_size = (300, 300)
      img.thumbnail(output_size)
      img.save(self.profile_picture.path)

class Listing(models.Model):
  title = models.CharField(max_length=200, null=False)
  description = models.CharField(max_length=2000, null=False)
  owner = models.CharField(max_length=30, null=False)

  def __str__(self):
    return self.title