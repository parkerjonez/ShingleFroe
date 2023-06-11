from flask import Blueprint, jsonify, request

text_analysis_bp = Blueprint('text_analysis_bp', __name__)

@text_analysis_bp.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.get_json()  

    # Return dummy data
    return jsonify({
        "status": "success",
        "original_text": data.get('text'),
        "analysis": {"word1": {"syllable_count": 3}, "word2": {"syllable_count": 2}}
    }), 200
