from django.contrib import admin
from .models import Lessons, LessonsComment
# Register your models here.

class CommentInLine(admin.TabularInline):
    model = LessonsComment
    extra = 0
class BlogsAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]

admin.site.register(LessonsComment)
admin.site.register(Lessons)