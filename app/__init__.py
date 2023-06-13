from flask import Flask, render_template, g
import fasttext

from app.routes.text_segmentation import text_segmentation_bp 
from app.routes.text_analysis import text_analysis_bp
from app.routes.health_check import health_check_bp
from app.routes.landing_page import landing_page_bp
from app.routes.language_detection import language_detection_bp

# Load the FastText model as a global variable since the model is large and will take time to load
fasttext_model = fasttext.load_model("app/models/lid.176.bin")

def create_app():
    app = Flask(__name__)

    @app.before_request
    def before_request():
        # Set the FastText model into the application context for each request
        g.fasttext_model = fasttext_model

    # Register blueprints
    app.register_blueprint(language_detection_bp)
    app.register_blueprint(text_segmentation_bp)  
    app.register_blueprint(text_analysis_bp)
    app.register_blueprint(health_check_bp)
    app.register_blueprint(landing_page_bp)
    
    return app
