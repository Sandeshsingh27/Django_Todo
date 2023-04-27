from django.shortcuts import render, HttpResponse
from home import models

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
    return render(request, 'tasks.html')
