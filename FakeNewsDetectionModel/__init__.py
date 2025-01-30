from flask import Flask
from routes import init_routes
from models import init_model

def create_app():
    app = Flask(__name__)
    init_routes(app)
    init_model(app)
    return app
