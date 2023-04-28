from django.shortcuts import render, HttpResponse, redirect
from home import models
# from .models import *

# Create your views here.

def index(request):
    context={'success':False}
    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['desc']

        data=models.Task(title=title, desc=desc)
        data.save()
        context={'success':True}
        print('user saved')
    return render(request, 'index.html', context)

def tasks(request):
    alltasks=models.Task.objects.all()
    context={'tasks':alltasks}
    return render(request, 'tasks.html', context)

def edit(request, pk):
    tasks=models.Task.objects.get(id=pk)
    context={'tasks':tasks}

    # if(request.POST.get('update')):
    #     update(pk)

    return render(request, 'edit.html', context)

def update(request, pk):
    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        complete=request.POST['complete']
        task = models.Task.objects.get(id=pk)
        task.title=title
        task.desc=desc
        task.complete=complete
        task.save()
        context={'success':True}
        print('task updated')
        # return redirect('/tasks')

    return render(request, 'tasks.html', context)

def delete(request, pk):
	item = models.Task.objects.get(id=pk)

	if item:
		item.delete()
		return redirect('/tasks')

	context = {'item':item}
	return render(request, 'tasks.html', context)

