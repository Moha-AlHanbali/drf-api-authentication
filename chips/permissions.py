from rest_framework import permissions

class IsUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow user of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.user is None:
            return True

        return obj.user == request.user