from django.urls import path, include
from .views import *
from chempionats import chempionats_url
from accounts.views import login, clientadd, log_out

urlpatterns = [
    path('', home, name='home'),
    path('haisdh1982h12dh1-dhdhaslhasdniid011dd1', flag, name='flag'),
    path('login_task', login_task, name='login_task'),
    path('hacking', hacking, name='hacking'),
    path('login', login, name='login'),
    path('client_register', clientadd, name='client_add'),
    path('logout', log_out, name='logout'),
    path('profile', profile, name='profile'),
    path('profile/<id>', hackers, name='hackers'),
    path('settings', settings, name='settings'),
    path('notifications', notifications, name='notifications'),
    path('users', users, name='users'),
    path('scoreboard', scoreboard, name='scoreboard'),
# Chempionats
    path('chempionats/', include(chempionats_url)),
# Challenges
    path('challenges', challenges, name='challenges'),
    path('challenges/<id>', challengetask, name='challengetask'),
    path('challenges/task/<id>', task, name='task')
]