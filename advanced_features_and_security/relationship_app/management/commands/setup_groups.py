from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from relationship_app.models import Book

class Command(BaseCommand):
    help = 'Create groups and assign permissions for Task 1'

    def handle(self, *args, **options):
        content_type = ContentType.objects.get_for_model(Book)
        
        # Get permissions
        can_view = Permission.objects.get(codename='can_view_book', content_type=content_type)
        can_create = Permission.objects.get(codename='can_create_book', content_type=content_type)
        can_edit = Permission.objects.get(codename='can_edit_book', content_type=content_type)
        can_delete = Permission.objects.get(codename='can_delete_book', content_type=content_type)
        
        # Create Groups
        viewers, created = Group.objects.get_or_create(name='Viewers')
        viewers.permissions.set([can_view])
        
        editors, created = Group.objects.get_or_create(name='Editors')
        editors.permissions.set([can_view, can_create, can_edit])
        
        admins, created = Group.objects.get_or_create(name='Admins')
        admins.permissions.set([can_view, can_create, can_edit, can_delete])
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created groups: Viewers, Editors, Admins')
        )