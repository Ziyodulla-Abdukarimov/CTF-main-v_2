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


class BlogsDetailView(DetailView):
    model = Blogs
    template_name = 'blogs/blog_detail.html'


def commentadd(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        if comment!=None:
            try:
                comment = Comment.comment=comment
                comment.save()
            except:
                messages.success(request, 'Bunday comment yozib bo`lmaydi!')
        else:
            messages.success(request, 'Comment bo\'sh bo\'lishi mumkin emas!')
    return render(request,'blogs/blog_detail.html')
