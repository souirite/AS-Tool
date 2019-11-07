from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from application.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    Bootstrap(app)

    db.init_app(app)
    bcrypt.init_app(app)

    from application.main.main import main
    from application.users.routes import users
    app.register_blueprint(main)
    app.register_blueprint(users)

    return app
