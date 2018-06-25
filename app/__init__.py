from flask import Flask

app = Flask(__name__) # magic method name, Flash will define the name

from app import routes
