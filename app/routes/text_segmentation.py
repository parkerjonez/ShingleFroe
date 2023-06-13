# app/routes/text_segmentation.py
from flask import Blueprint, jsonify, request
from marshmallow import Schema, fields, ValidationError
from app.services.text_segmentation_service import segment_text

class TextSegmentationSchema(Schema):
    transcript_id = fields.Str(required=True)
    language = fields.Str(required=False)
    text = fields.Str(required=True)

text_segmentation_bp = Blueprint('text_segmentation_bp', __name__)

@text_segmentation_bp.route('/segment', methods=['POST'])
def segment_text_route():
    schema = TextSegmentationSchema()
    try:
        data = schema.load(request.get_json())
    except ValidationError as e:
        return jsonify({"status": "error", "errors": e.messages}), 400

    result = segment_text(**data)

    return jsonify({"status": "success", **result}), 200