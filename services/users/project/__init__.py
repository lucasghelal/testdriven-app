import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from project.api.users import users_blueprint

# instatiate the db
db = SQLAlchemy()

def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # register blueprints
    app.register_blueprint(users_blueprint)


    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app