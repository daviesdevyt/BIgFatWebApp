from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from django.contrib.auth.decorators import login_required
from .models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember_me')
        remember = remember == 'on'
        user = authenticate(request, username=username, password=password)
        print(user)
        if user:
            login_user(request, user)
            return redirect('news')
        else:
            # TODO: Alert Password or username not correct
            pass
    return render(request, 'auth/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('confirm')
        if password == password2:
            print(username, password, password2)
            User.objects.create_user(username=username, password=password)
            return render(request, 'auth/login.html')
        else:
            # TODO: Passwords dont match
            pass
    return render(request, 'auth/login.html')

@login_required
def change_password(request):
    if request == "POST":
        password1 = request.POST.get("password")
        password2 = request.POST.get("confirm")
        if password1 == password2:
            request.user.set_password(password1)
            return redirect("news")
        else:
            # TODO: Alert Passwords dont match
            pass
    return render(request, "auth/change-password.html")

@login_required
def logout(request):
    logout_user(request)
    return redirect("login")