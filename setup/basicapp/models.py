from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class newUser(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)

    Portfolio=models.URLField(blank=True)
    Picture=models.ImageField(upload_to="profile_pics/",blank=True)
    def __str__(self):
        return str(self.user.username)
