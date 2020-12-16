from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

from .forms import TodoForm
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='users:login')
def Home(request):
    # return HttpResponse("Welcome to Todo Home Page!")
    todos = Todo.objects.all().order_by('-id')
    context = {
        'todos': todos
    }
    return render(request, 'todohome.html', context)

@login_required(login_url='login')
def TodoAdd(request):
    form = TodoForm(request.POST)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todo')
        else:
            return HttpResponse("Invalid submission!")
    return render(request, 'todoadd.html', {'form': form})

@login_required(login_url='login')
def TodoDelete(request, pk):
    todo_to_delete = Todo.objects.get(id=pk)
    todo_to_delete.delete()
    return redirect('todohome')

@login_required(login_url='login')
def TodoEdit(request, pk):
    todo_edit = Todo.objects.get(id=pk)
    form = TodoForm(request.POST, instance=todo_edit)
    if form.is_valid():
        form.save()
        return redirect('todohome')
    context = {'form': form}
    return render(request, 'todoadd.html', context)

@login_required(login_url='login')
def TodoComplete(request, pk):
    form = Todo.objects.get(id=pk)
    form.completed = True
    form.save()
    return redirect('todohome')
