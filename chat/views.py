from accounts.models import Client
from django.shortcuts import render
from django.views.generic import ListView
from .models import Chat
from django.contrib import messages

# Create your views here.

def chatdetail(request):
    if request.method == 'POST':
        message = request.POST['message']
        if message !=None:
            Chat(message=message, author=Client.objects.get(admin = request.user.id)).save()
        else:
            messages.success(request, 'Comment bo\'sh bo\'lishi mumkin emas!')
    context = {
        'chat':Chat.objects.all(),
    }
    return render(request, 'chat.html', context)
