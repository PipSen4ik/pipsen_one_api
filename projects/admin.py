from django.contrib import admin
from .models import Project, ProjectImage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ['image', 'alt_text', 'order']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'created_at']
    list_filter = ['category', 'status', 'project_type']
    search_fields = ['title', 'client']
    inlines = [ProjectImageInline]

    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description', 'long_description', 'category', 'status')
        }),
        ('Технологии и ссылки', {
            'fields': ('tech', 'source_url', 'demo_url')
        }),
        ('Изображения', {
            'fields': ('image',)
        }),
        ('Дополнительно', {
            'fields': ('client', 'project_type', 'start_date', 'end_date', 'features', 'apis_used', 'difficulty'),
            'classes': ('collapse',)
        }),
        ('Метаданные', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at']