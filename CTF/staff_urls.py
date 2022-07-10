from django.urls import path, include
from .staff import staff, log, users_admin_panel, scoreboard_admin_panel, errorlog

urlpatterns = [
    path('', staff, name='staff'),
    path('log', log, name='log'),
    path('users_admin_panel', users_admin_panel, name='users_admin_panel'),
    path('scoreboard_admin_panel', scoreboard_admin_panel, name='scoreboard_admin_panel'),
    path('errorlog', errorlog, name='errorlog'),
]