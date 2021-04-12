import os
from flask import Flask
from .models import config as config_db
from .blueprints import departments, colaborators, dependents

def create_app():
    app = Flask(__name__)

    path_db = os.path.join(app.instance_path, 'acmevita.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(path_db)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    config_db(app)

    app.register_blueprint(departments.bp)
    app.register_blueprint(colaborators.bp)
    app.register_blueprint(dependents.bp)

    return app
