from flask import Flask
from app.models import db
from main_route.routes import user_route


app = Flask(__name__, static_folder='../static',
            template_folder='../templates')


app.config.from_object('app.config.Config')
db.init_app(app)


with app.app_context():
    db.create_all()


app.register_blueprint(user_route)
