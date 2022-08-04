from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Lessons, LessonsComment
#comment un
from django.contrib import messages
from accounts.models import Client

# Create your views here.
class LessonsListView(ListView):
    model = Lessons
    template_name = 'lessons/lessons_list.html'


def lesonsdetail(request, pk):
    if request.method == 'POST':
        comm = request.POST['comment']
        if comm !=None:
            LessonsComment(lessons=Lessons.objects.get(id=pk), comment=comm, author=Client.objects.get(admin = request.user.id)).save()
        else:
            messages.success(request, 'Comment bo\'sh bo\'lishi mumkin emas!')
    context = {
        'lesson': Lessons.objects.get(id=pk),
        'comment': LessonsComment.objects.filter(lessons = Lessons.objects.get(id=pk)),
    }
    return render(request, 'lessons/lessons_detail.html', context)