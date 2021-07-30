from django.shortcuts import render, HttpResponseRedirect, reverse
from tweet.models import TweetModel
from twitteruser.models import TwitterUserModel


# Create your views here.
def profile_view(request, id):
    user = TwitterUserModel.objects.get(id=id)
    print(user)
    tweets = TweetModel.objects.filter(twitter=user).order_by('-date')
    friends = user.friends.all()
    total_friends = friends.count()
    total_tweets = tweets.count()

    return render(request, 'profile_view.html', {
        'user': user,
        'tweets': tweets,
        'friends': friends,
        'total_friends': total_friends,
        'total_tweets': total_tweets,
        })


def follow(request, id):
    user_ = request.user
    follow = TwitterUserModel.objects.get(id=id)
    user_.friends.add(follow)
    print(user_)
    return HttpResponseRedirect(reverse('profileview', args=(id,)))


def unfollow(request, id):
    user_ = request.user
    unfollow = TwitterUserModel.objects.get(id=id)
    user_.friends.remove(unfollow)
    print(user_)
    return HttpResponseRedirect(reverse('profileview', args=(id,)))
