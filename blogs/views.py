from django.shortcuts import render
from django.views.generic import ListView
from .models import Blogs

# Create your views here.

class BlogsListView(ListView):
    model = Blogs
    template_name = 'blogs_list.html'