from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signup(request):
    if request.method == 'POST':
        is_login = request.POST['is_login']
        if is_login == '1':
            username = request.POST['login_username']
            password = request.POST['login_password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(home)
            else:
                return HttpResponse('User not found')
        else:
            username = request.POST['signup_username']
            email = request.POST['signup_email']
            password = request.POST['signup_password']
            password2 = request.POST['signup_password2']
            if not username or not email or not password or not password2:
                return HttpResponse('Please fill in all fields')
            if password != password2:
                return HttpResponse('Password does not match')
            elif User.objects.filter(username=username).exists():
                return HttpResponse('Username already exists')
            elif User.objects.filter(email=email).exists():
                return HttpResponse('Email already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect(signup)
    return render(request, 'user/signup.html')


def signout(request):
    logout(request)
    return redirect(signup)


def home(request):
    if request.user.is_authenticated:
        return render(request, 'home/index.html', {'user': request.user})
    return redirect(signup)


def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'user/user_profile.html', {'user': request.user})
    return redirect(signup)