import os

class ProductionConfig:
    SECRET_KEY = os.getenv('app_sceret_code')
    WTF_CSRF_ENABLED = True
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    PREFERRED_URL_SCHEME = 'https'
