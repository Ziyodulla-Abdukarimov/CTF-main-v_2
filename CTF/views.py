from datetime import datetime
from django.shortcuts import redirect, render
from django.contrib import messages
from accounts.models import Task, Client, Journal, TaskLogin, ErrorLog, Log, Type
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q

# Create your views here.

def flag(request):
    return render(request, 'task/Flag.html')

def login_task(request):
    if request.method == 'POST':
        usernames=request.POST['username']
        password=request.POST['password']
        if "'" in usernames:
            print('go')
            context = {
                'task':TaskLogin.objects.all(),
            }
            return render(request, 'task/login-task.html', context)
        if ("admin" == usernames) and ("admin" == password):
            return redirect('flag')
    else:
        return render(request, 'task/login-task.html')
    return render(request, 'task/login-task.html')


def home(request):
    context = {
        'hackers_count': Client.objects.all().count(),
        'task_count': Task.objects.all().count(),
    }
    return render(request, 'index/index.html', context)


@login_required(login_url='login')
def hacking(request):
    hackers_count = Client.objects.all().count()
    task_count = Task.objects.all().count()
    res = Client.objects.order_by('-point', 'date')
    context = {
        'res': res,
        'hackers_count': hackers_count,
        'task_count': task_count,
    }
    return render(request, 'base.html', context)


@login_required(login_url='login')
def profile(request):
    cout_solved = Journal.objects.filter(hacker=Client.objects.get(admin=request.user.id)).count()
    task_solved = Journal.objects.filter(hacker=Client.objects.get(admin=request.user.id))
    try:
        error_count = ErrorLog.objects.filter(hacker=Client.objects.get(admin = request.user.id)).count()
    except:
        return redirect('home')
    context = {
        'cout_solved': cout_solved,
        'task_solved': task_solved,
        'error_count': error_count,
        'client': Client.objects.filter(admin=request.user.id),
    }
    return render(request, 'profile.html', context)


@login_required(login_url='login')
def hackers(request, id):
    hackers = Client.objects.filter(id=id)
    context = {
        'hackers': hackers,
        'cout_solved': Journal.objects.filter(hacker=Client.objects.get(admin=request.user.id)).count(),
        'error_count': ErrorLog.objects.filter(hacker=Client.objects.get(admin = request.user.id)).count(),
        'task_solved': Journal.objects.filter(hacker=Client.objects.get(admin=request.user.id)),
    }
    return render(request, 'hackers.html', context)



@login_required(login_url='login')
def settings(request):
    return render(request, 'settings.html')


@login_required(login_url='login')
def notifications(request):
    return render(request, 'notifications.html')


@login_required(login_url='login')
def users(request):
    context = {
        'client': Client.objects.all(),
    }
    return render(request, 'users.html', context)


@login_required(login_url='login')
def challenges(request):
    context = {
        'task': Type.objects.all(),
    }
    return render(request, 'challenges.html', context)


def challengetask(request, id):
    tasks = Task.objects.annotate(solved=Count('solvents', filter=Q(solvents__hacker__admin=request.user))).filter(type=id)
    context = {
        'task': tasks,
    }
    return render(request, 'tasks.html', context)


@login_required(login_url='login')
def scoreboard(request):
    res = Client.objects.order_by('-point', 'date')
    context = {
        'res': res,
    }
    return render(request, 'scoreboard.html', context)


@login_required(login_url='login')
def task(request, id):
    if request.method == 'POST':
        flag = request.POST['flag']
        if flag == Task.objects.get(id=id).flag:
            user_id = request.user.id
            if Journal.objects.filter(hacker=Client.objects.get(admin=user_id), task=Task.objects.get(id=id)).exists():
                messages.success(request, "Avval yechgansiz")
            else:
                Journal(hacker=Client.objects.get(admin=user_id),task=Task.objects.get(id=id),point=Task.objects.get(id=id).point).save()
                update_point = Client.objects.get(admin=request.user.id).point + Task.objects.get(id=id).point
                Client.objects.filter(admin=request.user.id).update(point=update_point, date=datetime.now())
                messages.info(request, 'To\'g\'ri javob')
                Log(hacker=Client.objects.get(id=request.user.id),task=Task.objects.get(id=id), flag=flag).save()
                return redirect('challenges')
        else:
            ErrorLog(hacker=Client.objects.get(id=request.user.id),task=Task.objects.get(id=id)).save()
            Log(hacker=Client.objects.get(id=request.user.id),task=Task.objects.get(id=id), flag=flag).save()
            messages.error(request, "Xato javob")
    context = {
        'task': Task.objects.filter(id=id),
        'test': Journal.objects.filter(hacker=Client.objects.get(admin=request.user.id), task=Task.objects.get(id=id)),
    }
    return render(request, 'task/task1.html', context)
