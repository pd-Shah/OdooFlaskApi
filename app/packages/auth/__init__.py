from flask import (
    Blueprint,
    jsonify,
    request,
)
from .logics import (
    odoo_version,
    odoo_login,
    odoo_create_portal_user,
)
from app.packages.error import error_check

bp = Blueprint('auth', __name__, )


@bp.route('/get-info')
@error_check
def version():
    odoo_server_info = odoo_version()
    return jsonify(status=200, message=odoo_server_info), 200


@bp.route('/login', methods=["POST", ])
@error_check
def login():
    user = request.get_json()
    uid = odoo_login(user)
    return jsonify(status=200, message={'uid': uid, }), 200


@bp.route('/create-portal-user', methods=["POST", ])
@error_check
def create_portal_user():
    uid = odoo_create_portal_user(request.get_json())
    return jsonify(status=200, message={'uid': uid, }), 200
