from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['created_at'] # Защита от случайного изменения
    # Добавляем красивое отображение сообщения
    fieldsets = (
        ('Контактная информация', {
            'fields': ('name', 'email')
        }),
        ('Сообщение', {
            'fields': ('message',)
        }),
        ('Метаданные', {
            'fields': ('created_at',),
            'classes': ('collapse',) # Сворачиваем блок
        }),
    )

    list_per_page = 25  # Количество записей на странице