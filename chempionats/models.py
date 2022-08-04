from django.db import models
from accounts.models import Client

# Create your models here.
class Chempionats(models.Model):
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=1000)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Chempionat_user(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    chempionats = models.ForeignKey(Chempionats, on_delete=models.CASCADE)
    point = models.IntegerField(default=0)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)


class Chempionat_task(models.Model):
    chempstitle = models.ForeignKey(Chempionats, on_delete=models.CASCADE, related_name='chemptask')
    title = models.CharField(max_length=100, verbose_name='Mavzu')
    body = models.CharField(max_length=1000, verbose_name='savol')
    text = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=500, blank=True, null=True)
    flag = models.CharField(max_length=50)
    point = models.IntegerField()

    def __str__(self):
        return self.title


class Chempionat_Journal(models.Model):
    user = models.ForeignKey(Chempionat_user, on_delete=models.CASCADE)
    task = models.ForeignKey(Chempionat_task, on_delete=models.CASCADE, related_name='solvents')
    point = models.IntegerField()

    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    