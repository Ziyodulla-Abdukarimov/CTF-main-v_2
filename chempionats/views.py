from datetime import datetime
from accounts.models import Client
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Chempionat_Journal, Chempionat_user, Chempionats, Chempionat_task

# Create your views here.


def chempionats(request):
    context = {
        'chempionats': Chempionats.objects.filter(start_date__lte=datetime.now(), end_date__gt=datetime.now()),
    }
    return render(request, 'chempionats/chempionats.html', context)

def chempionats_about(request, pk):
    if request.method == 'POST':
        Chempionat_user(user=Client.objects.get(admin=request.user.id), chempionats=Chempionats.objects.get(id=pk)).save()
    context = {
        'chempionats': Chempionats.objects.get(id=pk),
        'chempionat_user': Chempionat_user.objects.filter(user=request.user.id).exists(),
    }
    return render(request, 'chempionats/chempionats_about.html', context)


def chempionat_tasks(request, pk):
    context = {
        'task': Chempionat_task.objects.filter(chempstitle=pk),
    }
    return render(request, 'chempionats/chemptask.html', context)


def chempionat_tasks_open(request, pk):
    context = {
        'task': Chempionat_task.objects.filter(id=pk),
        'test': Chempionat_Journal.objects.filter(user=Chempionat_user.objects.get(user=request.user.id), task=Chempionat_task.objects.get(id=pk)),
    }
    return(request, 'chempionats/task.html', context)