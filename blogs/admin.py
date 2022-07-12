from django.contrib import admin
from .models import Blogs, Comment
# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
class BlogsAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(Comment)
admin.site.register(Blogs)