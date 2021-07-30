from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import TwitterUserModel


class TwitterUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = TwitterUserModel
        fields = UserCreationForm.Meta.fields + ('display_name',)
