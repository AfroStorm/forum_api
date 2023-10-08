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


class IoroPost(permissions.BasePermission):
    """
    IsOwnerOrReadOnly post (has_object_permission)
    """

    def has_object_permission(self, request, view, obj):
        """
        Checks if authenticated user is owner of the post
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.owner == request.user


class IoroUser(permissions.BasePermission):
    """
    IsOwnerOrReadOnly user (has_object_permission)
    """

    def has_object_permission(self, request, view, obj):
        """
        Checks if authenticated user is the user
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user


class IoroUserProfile(permissions.BasePermission):
    """
    IsOwnerOrReadOnly userprofile (has_object_permission)
    """

    def has_object_permission(self, request, view, obj):
        """
        Checks if authenticated user is the owner of the profile
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user


class IoroComment(permissions.BasePermission):
    """
    IsOwnerOrReadOnly comment (has_object_permission)
    """

    def has_object_permission(self, request, view, obj):
        """
        Checks if authenticated user is the owner of the comment
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.owner == request.user
