from django.contrib import admin

# Register your models here.
from article.models import (
    Article,
    Category,
    Tag,
)

@admin.action(description="Mark article published")
def make_published(modeladmin, request, queryset):
    queryset.update(status="pu")


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'status', 'created_at', 'category')
    list_filter = ('status',)
    actions = [make_published]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)