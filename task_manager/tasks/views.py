from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse

#タスクの一覧表示
@login_required
def task_list(request):
    tasks = Task.objects.filter(username=request.user).order_by('deadline')
    return render(request, 'tasks/index.html', {'tasks': tasks})

#タスクの新規作成
@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.username = request.user  #ログインユーザーを紐づける
            task.save()
            return redirect('tasks_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

#タスクの編集
@login_required
def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id, username=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

#タスクの削除
@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, username=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


def index(req):
  return HttpResponse('Hello World')


# Create your views here.
