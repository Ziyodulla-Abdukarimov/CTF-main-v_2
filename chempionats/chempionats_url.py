from django.urls import path
from .views import *

urlpatterns = [
    path('', chempionats, name='chempionats'),
    path('<pk>', chempionats_about, name='chempionats_about'),
    path('chempionat_tasks/<pk>', chempionat_tasks, name='chempionat_tasks'),
    path('chempionat_tasks/task/<pk>', chempionat_tasks_open, name='chempionat_tasks_open'),
]