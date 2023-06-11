import logging
from flask import Blueprint, jsonify, request
from langdetect import detect_langs

language_detection_bp = Blueprint('language_detection_bp', __name__)
logger = logging.getLogger(__name__)

@language_detection_bp.route('/detect', methods=['POST'])
def detect_language():
   
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
        # Detect the language of the text
        languages = detect_langs(text)
        most_likely_language = languages[0]  # Get the most likely language

        return jsonify({
            "status": "success",
            "original_text": text,
            "detected_language": most_likely_language.lang,
            "confidence": most_likely_language.prob
        }), 200
    except Exception as e:
        logger.exception("An error occurred during language detection.")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
