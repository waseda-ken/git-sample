from django.urls import path
from . import views

urlpatterns = [
    path('',                   views.task_list,   name='task_list'),   # /            → 一覧
    path('create/',            views.task_create, name='task_create'), # /create/     → 作成
    path('<int:task_id>/edit/',   views.task_update, name='task_update'), # /5/edit/    → 編集
    path('<int:task_id>/delete/', views.task_delete, name='task_delete'), # /5/delete/  → 削除
    path('calendar/',          views.task_calendar, name='task_calendar'), # /calendar/  → カレンダー
]