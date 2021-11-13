from flask import Flask

from app.config import DevConfig


#Initialising application
app = Flask(__name__)

# setting up configuration
app.config.from_object(DevConfig)

from app import views