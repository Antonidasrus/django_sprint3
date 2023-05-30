from django.contrib import admin

from blog.models import Category, Location, Post

admin.site.empty_value_display = 'Не задано'

admin.site.register(Location)
admin.site.register(Post)
admin.site.register(Category)
