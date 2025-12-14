from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Allow read-only to anyone. Write only to owner.
    """

    def has_object_permission(self, request, view, obj):
        # Safe methods allowed
        if request.method in permissions.SAFE_METHODS:
            return True
        # obj must have 'author' field
        return getattr(obj, "author", None) == request.user
