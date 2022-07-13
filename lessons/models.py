from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from accounts.models import Client

# Create your models here.

class Lessons(models.Model):
    title = models.CharField(max_length=150)
    summary = models.CharField(max_length=200,blank=True)
    body = models.TextField()
    photo = models.ImageField(upload_to='images/',blank=True)
#    video = models.
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('lessons_detail',args=[str(self.id)])


class LessonsComment(models.Model):
    lessons = models.ForeignKey(Lessons, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=150)
    author = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering =('-date',)
    def __str__(self):
        return self.comment