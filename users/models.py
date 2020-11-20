from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  title = models.CharField(default='Other', max_length=5)
  gender = models.CharField(default='Prefer Not to Say', max_length=20)
  account_type = models.CharField(default='Huntee', max_length=6)
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
