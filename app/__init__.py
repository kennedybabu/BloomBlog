from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):

    #Initialising application
    app = Flask(__name__)

     # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .request import configure_request
    configure_request(app)

    # setting up configuration
    app.config.from_object(config_options[config_name])
    # app.config.from_pyfile('config.py')   

    #intitialzing the flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    #settin config
    

    return app

