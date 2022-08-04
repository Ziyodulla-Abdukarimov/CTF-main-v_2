from django.urls import path
from .views import BlogsListView, blogdetail


urlpatterns=[
    path('<pk>',blogdetail,name='blog_detail'),
    path('',BlogsListView.as_view(),name='blogs_list')

]