from models.user import User
from flask import Blueprint, jsonify

blueprint = Blueprint('users', __name__)

@blueprint.route('/')
def get_user_data():
    user = User.query.filter_by(id=892).first()
    return jsonify({'success': 'true', 'user': user.json()})
