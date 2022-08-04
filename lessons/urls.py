from django.urls import path
from .views import lesonsdetail, LessonsListView


urlpatterns=[
    path('<int:pk>/',lesonsdetail,name='lessons_detail'),
    path('',LessonsListView.as_view(),name='lessons_list')

]