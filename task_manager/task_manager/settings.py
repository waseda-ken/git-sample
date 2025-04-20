"""
Django の設定ファイル (task_manager プロジェクト)

'django-admin startproject' を使用して Django 5.1.6 で生成されました。

このファイルの詳細については、以下を参照してください:
https://docs.djangoproject.com/en/5.1/topics/settings/

設定項目の完全な一覧とその値については、以下を参照してください:
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path

# プロジェクト内のパスを構築 (BASE_DIR / 'サブディレクトリ' という形で使用)
BASE_DIR = Path(__file__).resolve().parent.parent

# 開発用のクイックスタート設定 (本番環境には適さない)
# 詳細は https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/ を参照

# セキュリティ上の注意: 本番環境ではこの秘密鍵を適切に管理すること！
SECRET_KEY = 'django-insecure-fsq-++d(v6anad&6kc4&tan%_0w-ad7%ur7-o#-xnnppcb!j^y'

# セキュリティ上の注意: 本番環境では DEBUG を False にすること！
DEBUG = True

# 許可するホスト (デプロイ時には適切に設定すること)
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]

# アプリケーション定義
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ルート URL 設定
ROOT_URLCONF = 'task_manager.urls'

# テンプレート設定
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #　djangoに「このアプリを使うよ」と教える
        'DIRS': [os.path.join(BASE_DIR, 'development'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI アプリケーション設定
WSGI_APPLICATION = 'task_manager.wsgi.application'

# データベース設定
# 詳細は https://docs.djangoproject.com/en/5.1/ref/settings/#databases を参照
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# パスワードバリデーション
# 詳細は https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators を参照
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 国際化設定
# 詳細は https://docs.djangoproject.com/en/5.1/topics/i18n/ を参照
LANGUAGE_CODE = 'ja-JP'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# 静的ファイル (CSS, JavaScript, 画像) の設定
# 詳細は https://docs.djangoproject.com/en/5.1/howto/static-files/ を参照
STATIC_URL = 'static/'

#自前のCSS/JSを読み込むときの準備
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# デフォルトの主キー (PK) のフィールドタイプ
# 詳細は https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field を参照
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
