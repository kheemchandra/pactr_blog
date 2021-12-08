from django.contrib import admin

from .models import Comment, Post 

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'email', 'status')
    date_hierarchy = 'created'
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    search_fields = ['title', 'body']
    ordering = ('-created',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'commented')
    date_hierarchy = 'commented'
    raw_id_fields = ('post',)
    ordering = ('-commented',)                          

    