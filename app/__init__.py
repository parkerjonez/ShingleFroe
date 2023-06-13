from flask import Flask, current_app
import fasttext

from app.routes.text_segmentation import text_segmentation_bp 
from app.routes.text_analysis import text_analysis_bp
from app.routes.health_check import health_check_bp
from app.routes.landing_page import landing_page_bp
from app.routes.language_detection import language_detection_bp

def load_fasttext_model():
    # Load the FastText model
    fasttext_model = fasttext.load_model("app/models/lid.176.bin")
    return fasttext_model

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(language_detection_bp)
    app.register_blueprint(text_segmentation_bp)  
    app.register_blueprint(text_analysis_bp)
    app.register_blueprint(health_check_bp)
    app.register_blueprint(landing_page_bp)
    
    with app.app_context():
        # Load the FastText model and store it in the application context
        current_app.fasttext_model = load_fasttext_model()
    
    return app
