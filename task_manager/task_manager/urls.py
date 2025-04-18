"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),  # tasksアプリのURLを追加
    path('', views.task_list, name='task_list'),  # タスク一覧
    path('calendar/', views.task_calendar, name='task_calendar'),  # カレンダー表示（追加）
    path('create/', views.task_create, name='task_create'),  # タスク作成
    path('<int:task_id>/edit/', views.task_update, name='task_update'),  # タスク編集
    path('<int:task_id>/delete/', views.task_delete, name='task_delete'),  # タスク削除
]
