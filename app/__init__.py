from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
from .routes import api_bp

load_dotenv()
FRONT_URL = os.getenv("FRONT_URL")


def create_app():
    app = Flask(__name__)
    cors = CORS(app, resources={r"/api/*": {"origins": FRONT_URL}})

    app.register_blueprint(api_bp, url_prefix='/api')

    return app