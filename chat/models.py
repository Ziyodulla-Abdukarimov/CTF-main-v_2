from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Client
from django.urls import reverse

# Create your models here.

class Chat(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Client, on_delete=models.CASCADE)
    message = models.TextField()
    class Meta:
        ordering = ('-date',)
    def __str__(self):
        return self.message
    def get_absolute_url(self):
        return reverse('chat',args=[str(self.id)])

