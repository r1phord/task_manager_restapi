from rest_framework import generics
from rest_framework import permissions
from rest_framework import filters
from rest_framework import viewsets

from tasks.permissions import IsOwner
from tasks.models import Task, Tag
from tasks.serializers import TaskSerializer, TaskListSerializer, UserSerializer, TagSerializer


# class TagList(generics.ListCreateAPIView):
#     serializer_class = TagSerializer
#
#     def get_queryset(self):
#         user = self.request.user
#         return Tag.objects.filter(created_by=user)
#
#     def perform_create(self, serializer):
#         serializer.save(created_by=self.request.user)


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'tags__title']

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(owner=user)

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskListSerializer
        else:
            return TaskSerializer

    def add_tags_to_task(self, user, task, tag_names):
        for tag_name in tag_names:
            tag, created = Tag.objects.get_or_create(title=tag_name['title'], created_by=user)
            task.tags.add(tag)

    def perform_create(self, serializer):
        user = self.request.user
        task = serializer.save(owner=user)
        tag_names = self.request.data.get('tags', [])
        self.add_tags_to_task(user, task, tag_names)
        serializer.save()

    def perform_update(self, serializer):
        user = self.request.user
        task = self.get_object()
        tag_names = self.request.data.get('tags', [])
        self.add_tags_to_task(user, task, tag_names)
        serializer.save()


class RegisterUser(generics.CreateAPIView):
    serializer_class = UserSerializer
