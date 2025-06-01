from django.contrib import admin


# Register your models here.
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'updated_at')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)