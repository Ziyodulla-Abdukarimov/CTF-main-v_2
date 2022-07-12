from multiprocessing.connection import Client
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Blogs , Comment
#comment un
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login as authlogin, logout

# Create your views here.

class BlogsListView(ListView):
    model = Blogs
    template_name = 'blogs/blogs_list.html'

def blogdetail(request, pk):
    if request.method == 'POST':
        comment = request.POST['comment']
        id = request.POST['id']
        if comment !=None:
            Comment(blog=Blogs.objects.get(id=pk),comment=comment,author=Client.objects.get(admin=request.user.id)).save()
        else:
            messages.success(request, 'Comment bo\'sh bo\'lishi mumkin emas!')
    context = {
        'blog': Blogs.objects.get(id=pk),
        'comment': Comment.objects.filter(blog = Blogs.objects.get(id=pk)),
    }
    return render(request, 'blogs/blog_detail.html', context)