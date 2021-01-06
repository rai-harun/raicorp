from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import 

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm, ProfileForm
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from .models import Profile
# Create your views here.

def RegisterUser(request):
    form = CreateUserForm()
    customers = []
    users = User.objects.all()
    for user in users:
        customers.append(user.username)
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been successfully created')
            print('User created')
            return redirect('users:login')
        elif request.POST['username'] in customers:
            print('Same username')
            messages.error(request, 'Oops! Username is already taken. Try with new one.')
        else:
            print('wrong password')
            messages.error(request, 'Oops! something went wrong. Try again.')
    context = {'form': form}
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
            return redirect('index')
        else:
            messages.error(request, 'Enter the valid credentials')
    return render(request, 'login.html')

@login_required(login_url='users:login')
def LogoutUser(request):
    logout(request)
    return redirect('users:login')

def ProfileDetails(request, pk):
    user = User.objects.get(id=pk)
    profile_user = Profile.objects.get(user__id=pk)
    
    context = {
        'user':user,
        'profile_user': profile_user
    }
    # profile = Profile.objects.get(user=user)
    # profile = User.objects.filter(username=user).select_related('Profile')
    return render(request, 'profiledetails.html', context)
