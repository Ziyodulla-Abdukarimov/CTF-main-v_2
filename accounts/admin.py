from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Task)
admin.site.register(CustomUser)
admin.site.register(Client)
admin.site.register(Journal)
admin.site.register(TaskLogin)
admin.site.register(TaskLoginreg)
admin.site.register(Log)
admin.site.register(Type)