from django import forms
from django.contrib.auth.forms import UserCreationForm
from twitteruser.models import TwitterUserModel


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = TwitterUserModel
        fields = UserCreationForm.Meta.fields + ('display_name',)