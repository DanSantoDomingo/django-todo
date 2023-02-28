from rest_framework import permissions

from core import models


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        owner = obj.owner if type(obj) is models.ToDoList else obj.todo_list.owner
        return owner == request.user
