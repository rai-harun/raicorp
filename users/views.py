from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import 

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def RegisterUser(request):
    f = UserCreationForm(request.POST)
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account has been successfully created')
            # return redirect('users:login')
        else:
            # pass
            return HttpResponse(f'User cannot be created with the details provided. Try again.')
    context = {'form': f}
    return render(request, 'registeruser.html', context)

def LoginUser(request):
    # form 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success (request, f'Logged in successfully. Welcome {request.user}')
            return redirect('todohome')
        else:
            messages.error(request, 'Enter the valid credentials')
    return render(request, 'login.html')

def LogoutUser(request):
    logout(request)
    return redirect('users:login')