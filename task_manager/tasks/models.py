from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    username = models.ForeignKey(User, on_delete=models.CASCADE) #ユーザーと紐づけ
    title = models.CharField(max_length=255) #タスクのタイトル
    description = models.TextField(blank=True) #タスクの内容
    deadline = models.DateTimeField(null=True, blank=True) #締切日
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium') #優先度
    completed = models.BooleanField(default=False) #完了フラグ
    created_at = models.DateTimeField(auto_now_add=True) #作成日時
    updated_at = models.DateTimeField(auto_now=True) #更新日時

    def __str__(self):
        return self.title