from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
    # return HttpResponse("Welcome to Todo Home Page!")
    context = {
        
    }
    return render(request, 'home.html', context)