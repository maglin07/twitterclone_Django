from twitteruser.models import TwitterUserModel
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
import re

from tweet.forms import TweetForm
from tweet.models import TweetModel
from notification.models import Notification


# @login_required(login_url='login')
# def index(request):
#     all_tweets = TweetModel.objects.all().order_by("-date")
#     user = TwitterUserModel.objects.filter(username=request.user).first()
#     tweets = TweetModel.objects.filter(twitter=user).order_by('-date')
#     print(tweets)
#     friends = user.friends.all()
#     total_friends = friends.count()
#     total_tweets = tweets.count()

#     return render(request, 'index.html', {
#         'user': user,
#         'tweets': tweets,
#         'friends': friends,
#         'all_tweets': all_tweets,
#         'total_friends': total_friends,
#         'total_tweets': total_tweets,
#         })


@login_required(login_url='login')
def index(request):
    user_tweets = TweetModel.objects.filter(twitter=request.user).order_by("-date")
    friends = request.user.friends.all()
    following_tweets = TweetModel.objects.filter(twitter__in=friends).order_by("-date")
    tweets = user_tweets | following_tweets
    total_friends = friends.count()
    total_tweets = user_tweets.count()
    print(tweets)
    print('current_user', request.user)
    print(request.user.friends.all())
    return render(request, 'index.html', {
            'user': user_tweets,
            'tweets': tweets,
            'friends': friends,
            'total_friends': total_friends,
            'total_tweets': total_tweets,
    })


def post_tweet_view(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user_submit = request.user
            new_tweet = TweetModel.objects.create(
                text=data['text'],
                date=data['date'],
                twitter=user_submit
            )
            notification = re.findall(r'@(\w+)', data.get('text'))
            for notice in notification:
                user_new = TwitterUserModel.objects.get(username=notice)
                new_notice = Notification.objects.create(
                    receiver=user_new,
                    tweet=new_tweet,
                    )
                new_notice.save()
            return HttpResponseRedirect(reverse("home"))
    form = TweetForm()
    return render(request, 'post_tweet_form.html', {
            'form': form,
            })


def tweet_detail_view(request, id):
    tweets = TwitterUserModel.objects.filter(id=id).all()
    tweet = TweetModel.objects.get(id=id)
    context = {
        'tweets': tweets,
        'tweet': tweet,
        }
    return render(request, 'tweet_detail_view.html', context)