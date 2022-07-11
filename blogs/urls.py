from django.urls import path
from .views import BlogsListView, BlogsDetailView


urlpatterns=[
    path('<int:pk>/',BlogsDetailView.as_view(),name='blog_detail'),
    path('',BlogsListView.as_view(),name='blogs_list')

]