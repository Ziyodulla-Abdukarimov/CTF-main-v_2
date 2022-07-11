from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blogs

# Create your views here.

class BlogsListView(ListView):
    model = Blogs
    template_name = 'blogs/blogs_list.html'


class BlogsDetailView(DetailView):
    model = Blogs
    template_name = 'blogs/blog_detail.html'