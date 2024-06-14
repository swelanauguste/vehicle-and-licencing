from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        if self.first_name:
            return self.first_name
        return self.user.username