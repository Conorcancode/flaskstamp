from flask import Blueprint, url_for, render_template

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('index.html')