from django.contrib import admin

# Register your models here.

from .models import *

class StampAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photos', 'in_stock')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('in_stock',)
    list_filter = ('in_stock',)
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'news_name')
    list_display_links = ('id', 'news_name')
    search_fields = ('news_name', 'n_content')

admin.site.register(Stamp, StampAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)