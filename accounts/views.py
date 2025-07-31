from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def home(request):
    return render(request, 'accounts/home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check if user exists
        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/signup.html', {'error': 'Username already taken'})

        # Create the user
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('home')

    return render(request, 'accounts/signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})

    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')
