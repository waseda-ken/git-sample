from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 管理画面
    path('admin/', admin.site.urls),

    # Django 標準の認証機能（ログイン/ログアウト/パスワード変更など）
    path('accounts/', include('django.contrib.auth.urls')),

    # tasks アプリの URLconf を丸ごと読み込む
    path('', include('tasks.urls')),  
]
