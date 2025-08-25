from rest_framework.permissions import BasePermission


class IsRegisteredPermission(BasePermission):
    def has_permission(self, request, view):
        return request.telegram_user is not None