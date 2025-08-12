from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage


class Project(models.Model):
    STATUS_CHOICES = [
        ('in-progress', 'В работе'),
        ('frozen', 'Заморожен'),
        ('completed', 'Завершен'),
        ('draft', 'Черновик'),
        ('archived', 'В архиве'),
    ]
    CATEGORY_CHOICES = [
        ('All', 'All'),
        ('React', 'React'),
        ('Vue', 'Vue'),
        ('Angular', 'Angular'),
        ('Node.js', 'Node.js'),
        ('TypeScript', 'TypeScript'),
        ('Fullstack', 'Fullstack'),
        ('Mobile', 'Mobile'),
    ]
    title = models.CharField(verbose_name='Название', max_length=200)
    description = models.TextField(verbose_name='Описание')
    long_description = models.TextField(
        verbose_name='Полное описание',
        blank=True,
        null=True,
        help_text="Подробное описание проекта (поддержка Markdown)"
    )
    tech = models.JSONField(
        verbose_name='Технологии',
        help_text="Список технологий, например: ['React', 'Redux']"
    )
    category = models.CharField(
        verbose_name='Категория',
        max_length=20,
        choices=CATEGORY_CHOICES
    )
    status = models.CharField(
        verbose_name='Статус',
        max_length=20,
        choices=STATUS_CHOICES
    )
    # Основное изображение (превью)
    image = models.ImageField(
        verbose_name='Основное изображение',
        upload_to='projects/%Y/%m/',
        blank=True,
        null=True,
        storage=MediaCloudinaryStorage(),
        help_text="Превью проекта (главная картинка в карточке)"
    )
    # Ссылки
    source_url = models.URLField(
        verbose_name='Ссылка на исходный код',
        blank=True,
        null=True,
        help_text="GitHub/GitLab репозиторий"
    )
    demo_url = models.URLField(
        verbose_name='Ссылка на демо',
        blank=True,
        null=True,
        help_text="Прямая ссылка на запущенный проект (например, Vercel)"
    )
    # Дополнительная информация
    client = models.CharField(
        verbose_name='Клиент / Цель',
        max_length=100,
        blank=True,
        null=True,
        help_text="Для кого был сделан проект"
    )
    project_type = models.CharField(
        verbose_name='Тип проекта',
        max_length=20,
        choices=[
            ('personal', 'Личный'),
            ('freelance', 'Фриланс'),
            ('team', 'Командный'),
            ('work', 'Рабочий'),
        ],
        blank=True,
        null=True
    )
    start_date = models.DateField(verbose_name='Дата начала', blank=True, null=True)
    end_date = models.DateField(verbose_name='Дата окончания', blank=True, null=True)
    features = models.JSONField(
        verbose_name='Ключевые особенности',
        blank=True,
        null=True,
        help_text='["PWA", "Аутентификация", "Оффлайн-режим"]'
    )
    apis_used = models.JSONField(
        verbose_name='Используемые API',
        blank=True,
        null=True,
        help_text='["OpenWeather API", "Stripe"]'
    )
    difficulty = models.PositiveSmallIntegerField(
        verbose_name='Сложность (1-5)',
        blank=True,
        null=True,
        help_text='Оценка сложности проекта'
    )
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='gallery',
        verbose_name='Проект'
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='projects/gallery/%Y/%m/',
        storage=MediaCloudinaryStorage()
    )
    alt_text = models.CharField(
        verbose_name='Подпись (alt)',
        max_length=200,
        blank=True,
        null=True
    )
    order = models.PositiveIntegerField(
        verbose_name='Порядок',
        default=0,
        help_text='Чем меньше — тем выше в галерее'
    )

    class Meta:
        verbose_name = "Изображение проекта"
        verbose_name_plural = "Галерея проектов"
        ordering = ['order']

    def __str__(self):
        return f"{self.project.title} — Изображение {self.order}"