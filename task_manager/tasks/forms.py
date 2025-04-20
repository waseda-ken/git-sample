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
        fields = ['title','description','due_date','priority','completed','created_at','updated_at']
        # フォームのラベルを日本語に変更
        labels = {
            'title': 'タスク名',
            'description': '詳細',
            'due_date': '締切日',
            'priority': '優先度',
            'completed': '完了',
            'created_at': '作成日時',
            'updated_at': '更新日時'
        }
        # フォームのヘルプテキストを日本語に変更
        help_texts = {
            'title': 'タスクのタイトルを入力してください。',
            'description': 'タスクの詳細を入力してください。',
            'due_date': 'タスクの締切日を選択してください。',
            'priority': 'タスクの優先度を選択してください。',
            'completed': 'タスクが完了した場合はチェックを入れてください。',
            'created_at': 'タスクが作成された日時です。',
            'updated_at': 'タスクが最後に更新された日時です。'
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
            'title': forms.TextInput(        # 単行テキスト入力
                attrs={'class': 'form-control', 'placeholder': 'タイトルを入力'}
            ),
            'description': forms.Textarea(   # 複数行テキスト入力
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': '詳細を入力（任意）'}
            ),
            'due_date': forms.DateInput(     # カレンダー付き日付入力
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'priority': forms.Select(        # ドロップダウン選択
                attrs={'class': 'form-select'}
            ),
            'completed': forms.CheckboxInput(  # チェックボックス
                attrs={'class': 'form-check-input'}
            ),
        }
