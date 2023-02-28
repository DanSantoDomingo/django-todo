from rest_framework import viewsets, permissions
from core.models import ToDoList, ToDoItem
from core.api.permissions import IsOwner
from core.api.serializers import ToDoListSerializer, ToDoItemSerializer


class ToDoItemViewSet(viewsets.ModelViewSet):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]


class ToDoListViewSet(viewsets.ModelViewSet):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
