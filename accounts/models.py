from django.db import models
from django.contrib.auth.models import User

from PIL import Image
from os.path import join, exists
from os import remove

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    filename = "{0}.{1}".format(str(instance.user), filename.split(".")[-1])
    filename = 'profile_pics/user_{0}/{1}'.format(instance.user.id, filename)
    if exists(join("media", filename)):
        remove(join("media", filename))
    return filename

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to=user_directory_path)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)