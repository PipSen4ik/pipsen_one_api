from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates a superuser if one does not already exist'

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if not username or not email or not password:
            self.stdout.write(
                self.style.WARNING('Superuser env vars missing. Skipping creation.')
            )
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.SUCCESS(f'Superuser "{username}" already exists.')
            )
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        self.stdout.write(
            self.style.SUCCESS(f'Superuser "{username}" created successfully.')
        )