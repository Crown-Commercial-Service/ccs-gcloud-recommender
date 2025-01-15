import os

class Config:
    """Base configuration with default settings."""
    SECRET_KEY = os.getenv('app_sceret_code')  # Replace with a secure key for production
    WTF_CSRF_ENABLED = True  # Enable CSRF protection
    SESSION_COOKIE_SECURE = False  # Secure cookies, should be True in production
    REMEMBER_COOKIE_SECURE = False  # Secure "remember me" cookies
    PREFERRED_URL_SCHEME = 'http'  # Use 'https' in production
    DEBUG = False  # Debug mode disabled by default

class ProductionConfig(Config):
    """Configuration for production."""
    SECRET_KEY = os.getenv('app_sceret_code')  # Replace with a secure key
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    PREFERRED_URL_SCHEME = 'https'

class TestingConfig(Config):
    """Configuration for testing."""
    TESTING = True
    WTF_CSRF_ENABLED = False  # Disable CSRF for easier testing

# You can dynamically load configs like this if needed
config_dict = {
    'production': ProductionConfig,
    'development': 'config.development.DevelopmentConfig',
    'testing': TestingConfig,
}
