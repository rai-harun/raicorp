from django.shortcuts import render, redirect
from django.http import HttpResponse
from todo.models import Todo

from .forms import TodoForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.
@login_required(login_url='users:login')
def Home(request):
    # return HttpResponse("Welcome to Todo Home Page!")
    # todos = Todo.objects.get(user__id=pk).order_by('-id')
    todos = Todo.objects.filter(user__id=request.user.id).order_by('-created_at')
    context = {
        'todos': todos
    }
    return render(request, 'todohome.html', context)

@login_required(login_url='login')
def TodoAdd(request):
    form = TodoForm(request.POST)
    if request.method == 'POST':
        # form = TodoForm(request.POST, request.FILES, instance=request.user.todo)
        form = TodoForm(request.POST, instance=request.user)
        if form.is_valid():
            title = form.cleaned_data.get('title','')
            Todo.objects.create(title=title, user=request.user)
            print(title)
            form.save()
            messages.success(request, "A todo has been created!")
            # return redirect('todohome')
            # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            # return HttpResponseRedirect('/todo/'+str(request.user.id)+'/')
            response = redirect('todohome')
            return response
        else:
            messages.error(request, "A todo could not be created! Try again.")
            # return HttpResponse("Invalid submission!")
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
