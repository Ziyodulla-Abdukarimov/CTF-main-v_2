from accounts.models import Client
from django.shortcuts import render
from django.views.generic import ListView
from .models import Blogs , Comment
#comment un
from django.contrib import messages

# Create your views here.

class BlogsListView(ListView):
    model = Blogs
    template_name = 'blogs/blogs_list.html'

def blogdetail(request, pk):
    if request.method == 'POST':
        comm = request.POST['comment']
        if comm !=None:
            Comment(blog=Blogs.objects.get(id=pk), comment=comm, author=Client.objects.get(admin = request.user.id)).save()
        else:
            messages.success(request, 'Comment bo\'sh bo\'lishi mumkin emas!')
    context = {
        'blog': Blogs.objects.get(id=pk),
        'comment': Comment.objects.filter(blog = Blogs.objects.get(id=pk)),
    }
    return render(request, 'blogs/blog_detail.html', context)