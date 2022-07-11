from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('', chempionats, name='chempionats'),
    path('<pk>', chempionats_about, name='chempionats_about'),
    path('chempionat_tasks/<pk>', chempionat_tasks, name='chempionat_tasks'),
    path('chempionat_tasks/<id>/task/<pk>', chempionat_tasks_open, name='chempionat_tasks_open'),
    path('<pk>/chempionats_scoreboard/', chempionats_scoreboard, name='chempionats_scoreboard'),
    path('<pk>/chempionats_rating', chempionats_rating, name='chempionats_rating'),
]