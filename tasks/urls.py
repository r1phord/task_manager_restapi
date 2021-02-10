from django.urls import path

from tasks import views


urlpatterns = [
    path('', views.TaskList.as_view(), name='tasks-list'),
    path('tags/', views.TagList.as_view(), name='tags-list'),
    path('task/<int:pk>', views.TaskDetail.as_view(), name='detail-task')
]
