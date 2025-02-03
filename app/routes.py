from flask import Flask
from app.controllers.receipt_controller import receipt_bp

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.register_blueprint(receipt_bp)
    return app
