from django.urls import path
from .views import LessonsDetailView, LessonsListView


urlpatterns=[
    path('<int:pk>/',LessonsDetailView.as_view(),name='lessons_detail'),
    path('',LessonsListView.as_view(),name='lessons_list')

]