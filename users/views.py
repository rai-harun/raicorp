from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import 

# Create your views here.

def RegisterUser(request):
    context = {}
    return render(request, 'registeruser.html', context)

def LoginUser(request):
    # form 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todohome')
        else:
            return HttpResponse('Invalid login credentials :(')
    return render(request, 'login.html')

def LogoutUser(request):
    logout(request)
    return redirect('users:login')