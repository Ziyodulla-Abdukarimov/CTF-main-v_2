from datetime import datetime
from accounts.models import Client
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Chempionat_Journal, Chempionat_user, Chempionats, Chempionat_task
from django.db.models import Count, Q

# Create your views here.


def chempionats(request):
    context = {
        'chempionats': Chempionats.objects.filter(start_date__lte=datetime.now(), end_date__gt=datetime.now()),
    }
    return render(request, 'chempionats/chempionats.html', context)

def chempionats_about(request, pk):
    print(Chempionat_user.objects.filter(user=request.user.id).exists())
    if request.method == 'POST':
        Chempionat_user(user=Client.objects.get(admin=request.user.id), chempionats=Chempionats.objects.get(id=pk)).save()
    context = {
        'chempionats': Chempionats.objects.get(id=pk),
        'chempionat_user': Chempionat_user.objects.filter(user=Client.objects.get(admin=request.user.id)).exists(),
    }
    return render(request, 'chempionats/chempionats_about.html', context)


def chempionat_tasks(request, pk):
    context = {
        'tasks': Chempionat_task.objects.annotate(solved=Count('solvents', filter=Q(solvents__user__user__admin=request.user))),
        'task': Chempionat_task.objects.filter(chempstitle=pk),
        'chempionat_id': Chempionats.objects.get(id=pk).id,
    }
    return render(request, 'chempionats/chemptask.html', context)


def chempionat_tasks_open(request, id, pk):
    if request.method == 'POST':
        flag = request.POST['flag']
        if flag == Chempionat_task.objects.get(id=pk).flag:
            user_id = Client.objects.get(admin=request.user.id)
            if Chempionat_Journal.objects.filter(user=Chempionat_user.objects.get(user=user_id), task=Chempionat_task.objects.get(id=pk)).exists():
                messages.success(request, "Avval yechgansiz")
            else:
                Chempionat_Journal(user=Chempionat_user.objects.get(user=user_id),task=Chempionat_task.objects.get(id=pk),point=Chempionat_task.objects.get(id=pk).point).save()
                update_point = Chempionat_user.objects.get(user=user_id).point + Chempionat_task.objects.get(id=pk).point
                Chempionat_user.objects.filter(user=user_id).update(point=update_point)
                messages.info(request, 'To\'g\'ri javob')
        else:
            messages.error(request, "Xato javob")
    context = {
        'task': Chempionat_task.objects.filter(id=pk),
        'test': Chempionat_Journal.objects.filter(user=Chempionat_user.objects.get(user=Client.objects.get(admin=request.user.id)), task=Chempionat_task.objects.get(id=pk)),
    }
    return render(request, 'chempionats/task.html', context)


def chempionats_scoreboard(request, pk):
    context = {
        'chempionats': Chempionats.objects.get(id=pk),
        'chempionat_user': Chempionat_user.objects.filter(user=request.user.id).exists(),
        'chempionat_user_all': Chempionat_user.objects.all(),
    }
    return render(request, 'chempionats/chempionats_scoreboard.html', context)


def chempionats_rating(request, pk):
    context = {
        'chempionats': Chempionats.objects.get(id=pk),
        'chempionat_user': Chempionat_user.objects.filter(user=request.user.id).exists(),
        'chempionat_user_all': Chempionat_user.objects.all(),
    }
    return render(request, 'chempionats/chempionats_rating.html', context)