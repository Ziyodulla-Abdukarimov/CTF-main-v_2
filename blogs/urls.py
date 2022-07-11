from django.urls import path
from .views import BlogsListView


urlpatterns=[
    path('',BlogsListView.as_view(),name='blogs_list')
]