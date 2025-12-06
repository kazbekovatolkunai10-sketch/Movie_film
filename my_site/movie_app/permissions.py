from rest_framework import permissions

class CheckStatus(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.status == 'pro':
            return True
        elif request.user.status == 'simple' and obj.status_movie == 'simple':
            return True
        return False

class CheckPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status == 'pro':
            return True
        else:
            return False