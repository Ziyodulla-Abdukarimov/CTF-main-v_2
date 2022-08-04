from django.http import HttpResponse, JsonResponse
from accounts.models import Client
from django.shortcuts import render
from .models import Chat

# Create your views here.

def chatdetail(request):
    return render(request, 'chat.html')

def getmessage(request):
    messages = Chat.objects.all()[:50]
    return JsonResponse({"messages": list(messages.values())})

def send(request):
    textarea = request.POST['textarea']
    Chat(message=textarea, author=Client.objects.get(admin = request.user.id)).save()
    return HttpResponse('Yuborildi')