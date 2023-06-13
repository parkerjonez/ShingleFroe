# app/routes/language_detection.py
import logging
from flask import Blueprint, jsonify, request, g
from app.services.language_detection_service import detect_language

language_detection_bp = Blueprint('language_detection_bp', __name__)
logger = logging.getLogger(__name__)

@language_detection_bp.route('/detect', methods=['POST'])
def detect_language_route():
    # Access the FastText model from the application context
    fasttext_model = g.fasttext_model

    data = request.get_json()

    if not data:
        return jsonify({
            "status": "error",
            "message": "Request body is missing."
        }), 400

    text = data.get('text')

    if not text:
        return jsonify({
            "status": "error",
            "message": "The 'text' field is missing in the request body."
        }), 400

    try:
        result = detect_language(fasttext_model, text)
        return jsonify({"status": "success", **result}), 200
    except Exception as e:
        logger.exception("An error occurred during language detection.")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
