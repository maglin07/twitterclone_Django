from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUserModel


# Create your models here.
class TweetModel(models.Model):
    text = models.TextField(max_length=140)
    date = models.DateTimeField(default=timezone.now)
    twitter = models.ForeignKey(TwitterUserModel, on_delete=models.CASCADE,
                                related_name="twitter", null=True)

    def __str__(self):
        return self.text

