from django.urls import path
from tweet.views import (index, post_tweet_view, tweet_detail_view)


urlpatterns = [
    path("", index, name='home'),
    path('tweet/', post_tweet_view, name="posttweet"),
    path('tweet/<int:id>/', tweet_detail_view, name="tweetview"),
    ]