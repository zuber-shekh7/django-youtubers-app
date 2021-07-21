from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import UserSignupForm, UserSigninForm


def signup(request):
    form = UserSignupForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:signin')
    return render(request, 'accounts/signup.html', context)


def signin(request):
    form = UserSigninForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = UserSigninForm(request.POST)
        if form.is_valid():
            print(dir(form))
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('accounts:dashboard')
    return render(request, 'accounts/signin.html', context)


@login_required
def dashboard(request):
    context = {
        'user': request.user,
    }
    return render(request, 'accounts/dashboard.html', context)


@login_required
def signout(request):
    logout(request)
    return redirect('accounts:signin')
