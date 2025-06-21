from flask import Blueprint
bp = Blueprint('token', __name__)
@bp.route('/token')
def get_token():
    return 'token info'