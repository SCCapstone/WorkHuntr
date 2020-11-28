from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from PIL import Image

class Profile(models.Model):

  def update_resume_filename(instance, filename):
    return 'resumes/' + f'{instance.user.username}_resume.pdf'

  user = models.OneToOneField(User, on_delete=models.CASCADE)
  title = models.CharField(default='Other', max_length=5)
  gender = models.CharField(default='Prefer Not to Say', max_length=20)
  account_type = models.CharField(default='Huntee', max_length=6)
  profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
  resume = models.FileField(default='default.pdf', upload_to=update_resume_filename, validators=[FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='Resume (.pdf only)')
  website = models.URLField(default='', max_length=200, blank=True)
  privacy = models.CharField(default='Public', max_length=10)

  def __str__(self):
    return f'{self.user.username} Profile'

  def save(self):
    super().save()
    img = Image.open(self.profile_picture.path)
    if img.height > 300 or img.width > 300:
      output_size = (300, 300)
      img.thumbnail(output_size)
      img.save(self.profile_picture.path)
