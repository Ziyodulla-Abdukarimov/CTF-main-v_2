from django.urls import path
from .views import chatdetail

urlpatterns = [
    path('',chatdetail,name='chat'),
]
