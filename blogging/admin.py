from django.contrib import admin
from blogging.models import Post, Category


# Register your models here.

class CategoryInline(admin.TabularInline):
    model = Category


class PostAdmin(admin.ModelAdmin):
    Inlines = [
        CategoryInline,

    ]


admin.site.register(Post)
admin.site.register(Category)
