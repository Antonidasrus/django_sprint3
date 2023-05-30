from django.contrib import admin

from blog.models import Category, Location, Post

admin.site.empty_value_display = 'Не задано'


class PostInline(admin.TabularInline):
    model = Post
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        PostInline,
    ]


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_published',
        'category',
        'location'
        )
    list_editable = (
        'is_published',
        'category',
        'location',
        )
    search_fields = ('title',)
    list_filter = ('is_published',)
    list_display_links = ('title',)


admin.site.register(Location)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
