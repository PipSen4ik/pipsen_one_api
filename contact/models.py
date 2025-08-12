from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100)
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Сообщение', max_length=1000)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.email}"

    class Meta:
        verbose_name = "Сообщение с формы"
        verbose_name_plural = "Сообщения с формы"
        # Сортировка по дате создания (новые сверху)
        ordering = ['-created_at']