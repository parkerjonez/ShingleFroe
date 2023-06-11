import logging

from flask import Blueprint, jsonify, request, g
from langdetect import detect_langs

language_detection_bp = Blueprint('language_detection_bp', __name__)
logger = logging.getLogger(__name__)


# Load FastText model
#fasttext_model = fasttext.load_model("app/models/lid.176.bin")


@language_detection_bp.route('/detect', methods=['POST'])
def detect_language():

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
        # Detect the language of the text with langdetect
        langdetect_languages = detect_langs(text)
        langdetect_most_likely_language = langdetect_languages[0]  # Get the most likely language

        # Detect the language of the text with FastText
        fasttext_prediction = fasttext_model.predict(text)[0][0]  # Get the predicted language
        fasttext_most_likely_language = fasttext_prediction.replace('__label__', '')  # Remove the '__label__' prefix

        return jsonify({
            "status": "success",
            "original_text": text,
            "langdetect": {
                "detected_language": langdetect_most_likely_language.lang,
                "confidence": langdetect_most_likely_language.prob
            },
            "fasttext": {
                "detected_language": fasttext_most_likely_language,
                "confidence": fasttext_model.predict(text)[1][0]
            }
        }), 200
    except Exception as e:
        logger.exception("An error occurred during language detection.")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
