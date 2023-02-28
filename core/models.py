from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ToDoList(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)


class ToDoItem(models.Model):
    todo_list = models.ForeignKey(
        ToDoList, on_delete=models.CASCADE, related_name="todos"
    )
    text = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
