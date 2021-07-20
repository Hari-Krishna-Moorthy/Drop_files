from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    print(instance, type(instance))
    print(instance.user, filename)
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Files(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    filename = models.CharField(max_length=255, default="")
    description = models.TextField(blank=True, default="" )
    date_added = models.DateTimeField(auto_now_add=True, )
    File = models.FileField(upload_to='documents/')
    # File = models.FileField(upload_to='upload/%Y/%m/%d/')
    # File = models.FileField(upload_to='user_directory_path')
    
    def __str__(self):
        return "{0} {1}".format(self.user.username, self.filename)