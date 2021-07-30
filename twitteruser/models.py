from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class TwitterUserModel(AbstractUser):
    display_name = models.CharField(max_length=50)
    friends = models.ManyToManyField('self', symmetrical=False)

    def __str__(self):
        return self.username

