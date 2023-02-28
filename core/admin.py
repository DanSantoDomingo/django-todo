from django.contrib import admin
from core import models

# Register your models here.
admin.site.register(models.ToDoItem)
admin.site.register(models.ToDoList)
