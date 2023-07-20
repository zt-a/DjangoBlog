from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name', 'time_create', 'time_update', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('name',)}


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('id', 'name', 'email', 'time_create', 'time_update', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name', 'time_create', 'time_update', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('name',)}


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'content', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', 'author')
    search_fields = ('id', 'name', 'author', 'time_create', 'time_update', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')

admin.site.register(Category, CategoryAdmin)
admin.site.register(ContactUsModel, ContactUsAdmin)
admin.site.register(TagModel, TagAdmin)
admin.site.register(BlogModel, BlogAdmin)
