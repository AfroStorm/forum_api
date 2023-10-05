from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response


# View permissions
class IsListOnly(permissions.BasePermission):
    """
    Only allows read on a list (has_permission)
    """

    def has_permission(self, request, view):
        """
        Checks if view.action is create
        """

        return view.action != 'create'


# Object permissions
class IsReadOnly(permissions.BasePermission):
    """
    Only allows read on an object (has_object_permission)
    """

    def has_object_permission(self, request, view, obj):
        """
        Restricts all users to read only for the object
        """
        if request.method in permissions.SAFE_METHODS:
            return True


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Only allows owner to modify an object (has_object_permission)
    """

    def has_object_permission(self, request, view, obj):
        """
        Checks if authenticated user is owner of the object
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
