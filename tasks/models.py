from datetime import datetime

from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=15)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='created_tags')


class Task(models.Model):
    owner = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date = models.DateField(default=datetime.today)
    tags = models.ManyToManyField(Tag, related_name='tasksByTag', blank=True)
