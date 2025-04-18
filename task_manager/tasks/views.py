from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse

import json
from django.utils.dateformat import DateFormat
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Task

# タスクの一覧を表示するビュー
@login_required  # ログインしているユーザーのみアクセス可能
def task_list(request):
    # ログインユーザーに紐づくタスクを取得し、期限順に並べる
    tasks = Task.objects.filter(username=request.user).order_by('deadline')
    return render(request, 'tasks/index.html', {'tasks': tasks})

# タスクの新規作成を行うビュー
@login_required
def task_create(request):
    if request.method == 'POST':  # フォームが送信された場合
        form = TaskForm(request.POST)  # フォームのデータを取得
        if form.is_valid():  # バリデーションチェック
            task = form.save(commit=False)  # データを保存せずにインスタンスを作成
            task.username = request.user  # ログインユーザーをタスクの作成者として設定
            task.save()  # タスクを保存
            return redirect('tasks_list')  # タスク一覧画面へリダイレクト
    else:
        form = TaskForm()  # フォームを新規作成
    return render(request, 'tasks/task_form.html', {'form': form})  # フォームを表示

# タスクの編集を行うビュー
@login_required
def task_update(request, task_id):
    # 指定されたIDのタスクを取得し、ログインユーザーのタスクであることを確認
    task = get_object_or_404(Task, id=task_id, username=request.user)
    if request.method == 'POST':  # フォームが送信された場合
        form = TaskForm(request.POST, instance=task)  # 既存のタスクをフォームに適用
        if form.is_valid():  # バリデーションチェック
            form.save()  # 変更を保存
            return redirect('tasks_list')  # タスク一覧画面へリダイレクト
    else:
        form = TaskForm(instance=task)  # 既存のタスク情報をフォームにセット
    return render(request, 'tasks/task_form.html', {'form': form})  # フォームを表示

# タスクの削除を行うビュー
@login_required
def task_delete(request, task_id):
    # 指定されたIDのタスクを取得し、ログインユーザーのタスクであることを確認
    task = get_object_or_404(Task, id=task_id, username=request.user)
    if request.method == 'POST':  # 削除が確定した場合
        task.delete()  # タスクを削除
        return redirect('task_list')  # タスク一覧画面へリダイレクト
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})  # 確認画面を表示

# シンプルなインデックスページ
# 動作確認用のHello World表示

def index(req):
    return HttpResponse('Hello World')


# カレンダービュー：タスクをカレンダー形式で表示する
@login_required
def task_calendar(request):
    # ログイン中ユーザーのタスクを取得
    tasks = Task.objects.filter(user=request.user)

    # FullCalendar用のイベントリストを作成
    events = []
    for task in tasks:
        if task.due_date:
            events.append({
                'title': task.title,  # カレンダー上に表示するタスク名
                'start': DateFormat(task.due_date).format('Y-m-d'),  # 日付（YYYY-MM-DD形式）
                'color': get_priority_color(task.priority),  # 優先度に応じた色を設定
            })

    # JSON形式のデータをテンプレートへ渡して表示
    return render(request, 'tasks/calendar.html', {
        'events_json': json.dumps(events)
    })

# 優先度に応じた色を返す関数
def get_priority_color(priority):
    if priority == 'high':
        return 'red'
    elif priority == 'medium':
        return 'green'
    else:
        return 'blue'  # 'low'の場合
