from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = 'Вы не являетесь создателем'

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        else:
            return False
