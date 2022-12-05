from django.contrib import admin
from .models import createBlog, comments

class blogAdmin(admin.ModelAdmin):
    list_display = ('title','intro','body','image','slog','date_added')

class commentAdmin(admin.ModelAdmin):
    list_display = ('body','email','date_added')

admin.site.register(createBlog, blogAdmin)
admin.site.register(comments, commentAdmin)