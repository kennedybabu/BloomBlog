from flask import Flask

from app.config import DevConfig


#Initialising application
app = Flask(__name__)

# setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views