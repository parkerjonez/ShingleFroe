from flask import Blueprint, jsonify, request

text_segmentation_bp = Blueprint('text_segmentation_bp', __name__)

@text_segmentation_bp.route('/segment', methods=['POST'])
def segment_text():
    data = request.get_json()  # Get JSON data from the request

    # Just return the dummy data for now
    return jsonify({
        "status": "success",
        "original_text": data.get('text'),
        "segments": ["This is a dummy segment.", "Here's another one."]
    }), 200
