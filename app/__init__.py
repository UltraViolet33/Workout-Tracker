import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()


def create_app(config_type=None):
    app = Flask(__name__)
    csrf.init_app(app)

    if config_type == None:
        config_type = os.getenv(
            'CONFIG_TYPE', default='config.DevelopmentConfig')

    app.config.from_object(config_type)

    initialize_extensions(app)
    register_blueprints(app)

    engine = sa.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    inspector = sa.inspect(engine)
    # # if not inspector.has_table("categories"):
    # with app.app_context():
    #     db.drop_all()
    #     db.create_all()

    return app


def initialize_extensions(app):
    db.init_app(app)


def register_blueprints(app):

    from .categories import categories
    app.register_blueprint(categories, url_prefix="/categories")

    from .exercices import exercises
    app.register_blueprint(exercises, url_prefix="/exos")

    from .sessions import sessions
    app.register_blueprint(sessions, url_prefix="/")
