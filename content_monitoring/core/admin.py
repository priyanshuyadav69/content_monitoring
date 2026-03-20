
from django.contrib import admin
from .models import Keyword, ContentItem, Flag

@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(ContentItem)
class ContentItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'source', 'last_updated']
    search_fields = ['title', 'body']


@admin.register(Flag)
class FlagAdmin(admin.ModelAdmin):
    list_display = ['keyword', 'content_item', 'score', 'status']
    list_filter = ['status']