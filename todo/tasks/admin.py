from django.contrib import admin

from .models import Category, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'category', 'priority', 'deadline', 'done',)
    search_fields = ('title',)
    list_filter = ('category', 'priority', 'done', 'deadline',)
    list_editable = ('category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
