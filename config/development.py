from config import Config
import os

class DevelopmentConfig(Config):
    """Configuration for development."""
    DEBUG = True  # Enable debug mode
    SESSION_COOKIE_SECURE = False  # Cookies not marked secure for local testing
    REMEMBER_COOKIE_SECURE = False  # Remember-me cookies not secure
    PREFERRED_URL_SCHEME = 'http'  # Local development usually uses HTTP
    SECRET_KEY = os.getenv('app_sceret_code')  # Replace with a key for development
