from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Task, Tag


class TagSerializer(serializers.PrimaryKeyRelatedField, serializers.ModelSerializer):
    def to_representation(self, value):
        return value.title

    class Meta:
        model = Tag
        fields = ['title']


class TaskListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(queryset=Tag.objects.all(), many=True, required=False)
    description = serializers.CharField(write_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'date', 'tags']


class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'date', 'tags']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'password']
