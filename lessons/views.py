from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Lessons

# Create your views here.
class LessonsListView(ListView):
    model = Lessons
    template_name = 'lessons/lessons_list.html'


class LessonsDetailView(DetailView):
    model = Lessons
    template_name = 'lessons/lessons_detail.html'
