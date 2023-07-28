from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_user
from .models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        remember = remember == 'on'
        user = authenticate(request, username=username, password=password)
        print(user)
        if user:
            login_user(request, user)
            return redirect('news')
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
    return render(request, 'auth/login.html')