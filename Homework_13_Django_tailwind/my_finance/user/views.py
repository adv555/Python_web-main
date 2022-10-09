from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return redirect('auth:login')


def login(request):
    print('LOGIN', request.user)
    return render(request, 'auth/login.html')


def logout(request):
    logout(request)
    return render(request, 'auth/login.html')


def register(request):
    print('REGISTER', request.user)
    return render(request, 'auth/register.html')
