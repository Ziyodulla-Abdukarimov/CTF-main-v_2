from django.urls import path
from .views import chatdetail, send, getmessage

urlpatterns = [
    path('',chatdetail,name='chat'),
    path('send', send, name='send'),
    path('getmessage/', getmessage, name='getmessage'),
]
