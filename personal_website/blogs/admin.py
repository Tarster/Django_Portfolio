from django.contrib import admin
from .models import Author, Post, Tag,Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'tags', 'date')

class TagAdmin(admin.ModelAdmin):
    list_display = ('caption',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'email')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment)
