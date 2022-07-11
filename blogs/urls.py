from django.urls import path
from .views import BlogsListView, BlogsDetailView


urlpatterns=[
    path('<int:pk>/',BlogsDetailView.as_view(),name='blogs_detail'),
    path('',BlogsListView.as_view(),name='blogs_list')

]