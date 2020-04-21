from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):

    def has_permission(self, request, view):
        print('Checking if user is author. User Role id - {}'.format(request.user.role))
        return True if request.user.role == 1 else False


class IsSuperAdmin(BasePermission):

    def has_permission(self, request, view):
        print('Checking if user is author. Is Super admin - {}'.format(request.user.is_superuser))
        return request.user.is_superuser

