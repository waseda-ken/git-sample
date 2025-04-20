from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    """
    Taskモデル用のフォーム定義。
    ModelFormを継承することで、モデルとフォームの連携を簡単に実現。
    """
    class Meta:
        model = Task
        # フォームに表示するモデルのフィールドを列挙
        fields = ['title','description','due_date','priority','completed']
        # フォームのラベルを日本語に変更

        labels = {
            'title': 'タスク名',
            'description': '詳細',
            'due_date': '締切日',
            'priority': '優先度',
            'completed': '完了',
        }

        # フォームのヘルプテキストを日本語に変更
        help_texts = {
            'title': 'タスクのタイトルを入力してください。',
            'description': 'タスクの詳細を入力してください。',
            'due_date': 'タスクの締切日を選択してください。',
            'priority': 'タスクの優先度を選択してください。',
            'completed': 'タスクが完了した場合はチェックを入れてください。',
        }
        # フォームのエラーメッセージを日本語に変更
        error_messages = {
            'title': {
                'required': 'タスク名は必須です。',
                'max_length': 'タスク名は255文字以内で入力してください。'
            },
            'description': {
                'max_length': '詳細は1000文字以内で入力してください。'
            },
            'due_date': {
                'invalid': '有効な日付を入力してください。'
            },
            'priority': {
                'invalid_choice': '無効な優先度が選択されました。'
            },
        }

        # 各フィールドに対応するHTMLウィジェットと属性を指定
        widgets = {
            # 単業テキスト入力
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'タイトルを入力'}
            ),

            # 複数行テキスト入力
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': '詳細を入力（任意）'}
            ),

            # カレンダー付き日付入力
            'due_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),

            # ドロップダウン選択
            'priority': forms.Select(
                attrs={'class': 'form-select'}
            ),

            # チェックボックス
            'completed': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
            ),

        }
