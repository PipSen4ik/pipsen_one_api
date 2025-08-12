# 🚀 DevPortfolio MG — Backend API

Универсальный Django-бэкенд для портфолио-сайта разработчика. Обеспечивает работу контактной формы и API для отображения проектов. Интегрирован с PostgreSQL, отправляет уведомления через Yandex SMTP, хранит изображения на Cloudinary и развёрнут в облаке Render.

[![Django](https://img.shields.io/badge/Django-4.2-blue?logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://www.python.org/)
[![REST Framework](https://img.shields.io/badge/DRF-3.15-red)](https://www.django-rest-framework.org/)
[![Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7.svg?logo=render)](https://render.com)

---

## 🌐 Демо

🔗 **Фронтенд**: [https://pipsen-one.vercel.app](https://pipsen-one.vercel.app)  
🛠️ **API**: [https://pipsen-one-api.onrender.com](https://pipsen-one-api.onrender.com)

---

## 💡 Технологии

- **Python 3.13.5**
- **Django 5.2.5** — основа бэкенда
- **Django REST Framework (DRF)** — API
- **PostgreSQL** — база данных
- **Yandex SMTP** — отправка email
- **Cloudinary** — хранение изображений проектов
- **Gunicorn** — WSGI-сервер
- **Render** — хостинг
- **CORS Headers** — безопасность кросс-доменных запросов
- **Django Decouple** — управление конфигурацией
- **Whitenoise** — раздача статики
- **Django Management Commands** — автоматизация задач

---

## ✨ Особенности

- 📨 **Контактная форма с уведомлениями**  
  Отправляет сообщения с сайта на email с красивым HTML-шаблоном, включая логотип и стилизованный дизайн. Поддерживает `reply-to` для удобного ответа.
- 🖼️ **Поддержка изображений в проектах**  
  Загрузка скриншотов и галерей проектов через `ImageField` с интеграцией Cloudinary. Поддержка нескольких изображений с сортировкой по порядку.
- 🗂️ **Гибкая категоризация проектов**  
  Теги: React, Vue, Node.js, Mobile, TypeScript, Fullstack и др. Удобная фильтрация.
- 🔄 **Статусы проектов**  
  Поддержка: В работе, Заморожен, Завершён, Черновик, В архиве.
- 🌍 **API с CORS**  
  Безопасный доступ с фронтенда (Vercel) через `django-cors-headers`.
- 📦 **Готов к развёртыванию в облаке**  
  Конфигурация для Render с секретами и сборкой.

---

## 🗂️ Структура проекта

```
pipsen_one_api/
├── contact/               # Модуль контактной формы
│   ├── models.py          # ContactMessage
│   ├── serializers.py     # Сериализация формы
│   ├── views.py           # API: /api/contact/send-email/
│   ├── urls.py            # Роутинг
│   ├── admin.py           # Админ-панель сообщений
│   ├── email_utils.py     # HTML-письма с вложением логотипа
│   └── templates/         # Шаблон email
├── projects/              # Модуль проектов
│   ├── models.py          # Project + ProjectImage (галерея)
│   ├── serializers.py     # Сериализация проектов с галереей
│   ├── views.py           # API: /api/projects/get-projects/
│   └── admin.py           # Управление проектами и изображениями
├── pipsen_one_api/        # Настройки, WSGI/ASGI, management commands
│   ├── settings.py        # Конфигурация с decouple и Cloudinary
│   ├── urls.py            # Главный роутер
│   ├── wsgi.py / asgi.py  # Запуск сервера
│   └── management/        # Команда create_admin
├── manage.py
├── .env                   # Локальные переменные (не в репозитории)
├── render.yaml            # Конфигурация для Render
├── runtime.txt            # Версия Python
├── requirements.txt       # Зависимости
└── LICENSE                # MIT License
```

---

## 🚀 Как запустить

### 1. Клонируйте репозиторий
```bash
git clone https://github.com/pipsen4ik/pipsen-one-api.git
cd pipsen-one-api
```

### 2. Создайте виртуальное окружение и установите зависимости
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

### 3. Настройте переменные окружения
Создайте файл `.env` в корне:
```env
SECRET_KEY=ваш_секретный_ключ
DEBUG=True
DB_NAME=name_db
DB_USER=user_db
DB_PASSWORD=ваш_пароль
DB_HOST=localhost
DB_PORT=5432
CLOUDINARY_NAME=ваш_cloud_name
CLOUDINARY_API_KEY=ваш_api_key
CLOUDINARY_API_SECRET=ваш_api_secret
EMAIL_HOST_USER=ваш_email@yandex.ru
EMAIL_HOST_PASSWORD=ваш_app_password
WEBSITE_URL=http://localhost:5173
```

### 4. Запустите миграции
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Создайте суперпользователя (для админки)
```bash
python manage.py createsuperuser
```

### 6. Запустите сервер
```bash
python manage.py runserver
```

> Админка: `http://localhost:8000/admin`  
> API: `http://localhost:8000/api/contact/send-email/` и `/api/projects/get-projects/`

---

## 📡 Примеры использования

### Отправка сообщения
```http
POST /api/contact/send-email/
Content-Type: application/json

{
  "name": "Иван Иванов",
  "email": "ivan@example.com",
  "message": "Отличная работа! Хочу сотрудничать."
}
```

**Ответ при успехе:**
```json
{
  "detail": "Сообщение успешно отправлено"
}
```

### Получение списка проектов
```http
GET /api/projects/get-projects/
```

**Ответ:**
```json
[
  {
    "id": 1,
    "title": "Сайт-портфолио",
    "description": "Мой первый проект...",
    "tech": ["React", "Tailwind", "Vercel"],
    "category": "React",
    "status": "completed",
    "image": "/media/projects/2025/08/screenshot.png",
    "source_url": "https://github.com/pipsen4ik/portfolio",
    "demo_url": "https://pipsen-one.vercel.app",
    "created_at": "2025-08-11T10:00:00Z",
    "gallery": [
      {
        "id": 1,
        "image": "/media/projects/gallery/2025/08/gallery1.png",
        "alt_text": "Главная страница",
        "order": 0
      }
    ]
  }
]
```

---

## 🔧 **Автоматизация на Render**
- Используется `render.yaml` для описания сервиса и базы данных.
- При деплое:
  - Устанавливаются зависимости
  - Выполняются миграции
  - Создаётся суперпользователь (если не существует)
  - Запускается Gunicorn

```yaml
startCommand: "python manage.py migrate --noinput && python manage.py create_admin || echo 'Superuser creation skipped' && gunicorn pipsen_one_api.wsgi:application"
```

---

## ⚠️ Важно

Этот проект — часть моего портфолио.  
Прямое копирование без указания авторства **запрещено**.

---

## 📄 Лицензия

Проект распространяется под лицензией [MIT](LICENSE), но **не предназначен для прямого коммерческого копирования**.  
Использование кода в коммерческих проектах разрешено только с указанием авторства и ссылкой на оригинал.  
Это портфолио-проект, адаптированный для демонстрации навыков.

---

## 📬 Контакты / Автор

- **Имя**: Михаил
- **Email**: samotokhin.m@ya.ru
- **GitHub**: [pipsen4ik](https://github.com/pipsen4ik)
- **Портфолио**: [https://pipsen-one.vercel.app](https://pipsen-one.vercel.app)
