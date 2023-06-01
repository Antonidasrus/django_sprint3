from django.contrib import admin

from blog.models import Category, Location, Post

admin.site.empty_value_display = 'Не задано'


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'is_published',
        'pub_date',
    )
    list_editable = (
        'is_published',
        'pub_date'
    )    
    search_fields = ('title', 'text')
    list_filter = ('pub_date',)
    list_display_links = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'slug',
    )
    list_editable = (
        'slug',
    )    
    search_fields = ('title', 'slug')
    list_filter = ('slug',)
    list_display_links = ('title',)


admin.site.register(Location)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
