from django.contrib import admin
from core.models import *

class BookmarkInline(admin.StackedInline):
    model = Bookmark
    extra = 1

class CollectionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Collection',               {'fields': ['name', 'is_private']}),
    ]
    inlines = [BookmarkInline]
    #list_display = ('name', 'rating', 'is_private', 'date_added')


admin.site.register(Collection, CollectionAdmin)
