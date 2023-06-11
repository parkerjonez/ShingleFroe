from flask import Blueprint, render_template

landing_page_bp = Blueprint('landing_page_bp', __name__)

@landing_page_bp.route('/', methods=['GET'])
def landing_page():
    return render_template('index.html')