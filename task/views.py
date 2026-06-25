from django.shortcuts import render
from .models import Task
# Create your views here.
def homepage(request):
    title = 'Home'
    tasks = Task.objects.all()

    return render(request, 'home.html', {'title': title, 'tasks': tasks})
