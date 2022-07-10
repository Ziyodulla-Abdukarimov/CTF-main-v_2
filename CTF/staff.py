from django.shortcuts import render
from accounts.models import Client, Log, Task, ErrorLog

def staff(request):
    context = {
        'client_count': Client.objects.all().count(),
        'task_count': Task.objects.all().count(),
        'res': Client.objects.all(),
    }
    return render(request, 'staff.html', context)


def log(request):
    context = {
        'log': Log.objects.all()
    }
    return render(request, 'staff/log.html', context)

def errorlog(request):
    context = {
        'errorlog': ErrorLog.objects.all(),
    }
    return render(request, 'staff/errorlog.html', context)


def users_admin_panel(request):
    context = {
        'client':Client.objects.all(),
        }
    return render(request, 'staff/users_admin_panel.html', context)


def scoreboard_admin_panel(request):
    res = Client.objects.order_by('-point', 'date')
    context = {
        'res': res,
    }
    return render(request, 'staff/scoreboard_admin_panel.html', context)