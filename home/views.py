from django.shortcuts import render, HttpResponse, redirect
from home import models
# from .models import *

# Create your views here.

def index(request):
    context={'success':False}
    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        try:
            data=models.Task(title=title, desc=desc)
            data.save()
            context={'success':True}
            print('user saved')
        except:
            return 'There was an issue adding your task'
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
    context={}
    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        task = models.Task.objects.get(id=pk)
        task.title=title
        task.desc=desc
        
        task.complete = True if request.POST.get('complete') else False

        task.save()
        context={'success':True}
        print('task updated')
        # return redirect('/tasks')

    tasks=models.Task.objects.all()
    context.update({'tasks':tasks})
    return render(request, 'tasks.html', context)

def delete(request, pk):
	item = models.Task.objects.get(id=pk)

	if item:
		item.delete()
		return redirect('/tasks')

	context = {'item':item}
	return render(request, 'tasks.html', context)

