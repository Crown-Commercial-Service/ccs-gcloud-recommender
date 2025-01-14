from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_talisman import Talisman

def create_app(config_class='config.production.ProductionConfig'):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Enable CSRF protection
    csrf = CSRFProtect(app)
    
    # Secure HTTP Headers with Flask-Talisman
    csp = {
        'default-src': "'self'",
        'img-src': "'self' data:",
        'script-src': "'self'",
        'style-src': "'self'"
    }
    Talisman(app, content_security_policy=csp)

    # Register Blueprints
    with app.app_context():
        from .routes import main
        app.register_blueprint(main)

    return app
