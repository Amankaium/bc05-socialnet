from django.contrib import admin
from posts.models import *


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'title', 'author', 
        'created_at', 'updated_at'
    ]
    list_filter = ['author', 'created_at']
    search_fields = [
        'title', 'content', 
        'author__first_name', 'author__last_name',
        'author__username',
    ]
    list_editable = ['title', 'author']
    
    


admin.site.register(Like)
