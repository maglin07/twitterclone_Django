from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, RegisterForm
from twitteruser.models import TwitterUserModel


# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = TwitterUserModel.objects.create_user(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register_form.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data.get('username')
            password = data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse("home")))

    form = LoginForm()
    return render(request, 'login_form.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")
