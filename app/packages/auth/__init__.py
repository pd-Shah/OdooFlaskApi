from flask import (
    Blueprint,
    jsonify,
    request,
    abort,
)
from .logics import (
    odoo_version,
    odoo_login,
    odoo_create_portal_user,
)

bp = Blueprint('auth', __name__, )


@bp.route('/get-info')
def version():
    try:
        odoo_server_info = odoo_version()
    except Exception as e:
        abort(status=400, )
    return jsonify(status=200, message=odoo_server_info), 200


@bp.route('/login')
def login():
    try:
        uid = odoo_login()
    except Exception as e:
        abort(status=400, )
    return jsonify(status=200, message={'uid': uid, }), 200


@bp.route('/create-portal-user', methods=["POST", ])
def create_portal_user():
    try:
        uid = odoo_create_portal_user(request.get_json())
    except Exception as e:
        abort(status=400, )
    return jsonify(status=200, message={'uid': uid, }), 200
