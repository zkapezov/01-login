from django.core.management.base import BaseCommand
from django.contrib.auth import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(username='admin', email='test@test.com', password='admin')
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save()