from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        username = 'admin'
        if not User.objects.filter(username=username).exists():
            user = User.objects.create(
                username=username,
                email='admin',
                first_name='Admin',
                last_name='Admin',
                is_superuser=True,
                is_staff=True,
                is_active=True
            )

            user.set_password('0000')
            user.save()
