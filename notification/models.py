from django.db import models
from twitteruser.models import TwitterUserModel
from tweet.models import TweetModel


# Create your models here.
class Notification(models.Model):
    receiver = models.ForeignKey(
        TwitterUserModel, on_delete=models.CASCADE, related_name="receiver")
    tweet = models.ForeignKey(TweetModel, on_delete=models.CASCADE,
                              related_name="tweet", null=True)
    has_readed = models.BooleanField(default=False)