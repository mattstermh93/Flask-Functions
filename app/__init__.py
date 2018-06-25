from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__) # magic method name, Flash will define the name

from app import routes

bootstrap = Bootstrap(app)
