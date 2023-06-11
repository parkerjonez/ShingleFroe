from flask import Blueprint, jsonify

health_check_bp = Blueprint('health_check_bp', __name__)

@health_check_bp.route('/health', methods=['GET'])
def health_check():
    # Return dummy data
    return jsonify({
        "status": "success",
        "message": "API is healthy"
    }), 200
