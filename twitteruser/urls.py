from django.urls import path
from twitteruser.views import (
    profile_view, follow, unfollow
)

urlpatterns = [
    path("profile/<int:id>/", profile_view, name='profileview'),
    path("following/<int:id>/", follow, name="following"),
    path("unfollow/<int:id>/", unfollow, name="unfollow"),
    ]