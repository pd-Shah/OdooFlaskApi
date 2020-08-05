from flask import Blueprint, jsonify
from .logics import get_version

bp = Blueprint('auth', __name__, )


@bp.route('/login')
def version():
    return jsonify(status=200, message=get_version()), 200
