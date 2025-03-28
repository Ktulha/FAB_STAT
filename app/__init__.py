from flask import Flask
from flask_migrate import Migrate
from .config import Config
from .models import db
# Correctly import the main_route blueprint
from main_route.routes import user_route


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)  # Initialize Migrate

    with app.app_context():
        db.create_all()

    app.register_blueprint(user_route)  # Register the main_route blueprint

    return app
