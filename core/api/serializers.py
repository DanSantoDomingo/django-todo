from rest_framework import serializers
from django.contrib.auth import get_user_model

from core.models import ToDoList, ToDoItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username")


class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ("id", "text", "completed", "todo_list")

    def validate(self, data):
        todo_list = data.get("todo_list", None)
        if not todo_list:
            raise serializers.ValidationError("Please enter the To Do list ID.")

        user = self.context["request"].user
        if user.id != todo_list.owner.id:
            raise serializers.ValidationError(
                "You're not allowed to add/edit a To Do in list that you do not own."
            )
        return data


class ToDoListSerializer(serializers.ModelSerializer):
    todos = ToDoItemSerializer(many=True, read_only=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = ToDoList
        fields = ("id", "title", "owner", "todos")
