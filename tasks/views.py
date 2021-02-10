from rest_framework import generics
from rest_framework import permissions
from rest_framework import filters

from tasks.permissions import IsOwner
from tasks.models import Task, Tag
from tasks.serializers import TaskSerializer, TaskListSerializer, UserSerializer, TagSerializer


class TagList(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Tag.objects.filter(created_by=user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskListSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'tags__title']

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(owner_id=user.id)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]


class RegisterUser(generics.CreateAPIView):
    serializer_class = UserSerializer
