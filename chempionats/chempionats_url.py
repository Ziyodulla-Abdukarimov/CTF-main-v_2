from django.urls import path
from .views import chempionats

urlpatterns = [
    path('', chempionats, name='chempionats')
]