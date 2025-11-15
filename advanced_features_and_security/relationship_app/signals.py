from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    if sender.name != "relationship_app":
        return

    groups = {
        "Admin": ["can_view", "can_create", "can_edit", "can_delete"],
        "Librarian": ["can_view", "can_edit"],
        "Member": ["can_view"],
    }

    for group_name, perms in groups.items():
        group, created = Group.objects.get_or_create(name=group_name)

        for perm_code in perms:
            try:
                perm = Permission.objects.get(codename=perm_code)
                group.permissions.add(perm)
            except Permission.DoesNotExist:
                pass
