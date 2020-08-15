from xmlrpc.client import Fault
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
    except Fault as e:
        code, error_message = e.faultCode, e.faultString.split('\n')[-2] + e.faultString.split('\n')[-1]
        return jsonify(status=code, message={"error_message": error_message, }), 500
    except Exception as e:
        code, error_message = e.args
        return jsonify(status=code, message={"error_message": error_message, }), 500
    return jsonify(status=200, message=odoo_server_info), 200


@bp.route('/login', methods=["POST", ])
def login():
    user = request.get_json()
    try:
        uid = odoo_login(user)
    except Fault as e:
        code, error_message = e.faultCode, e.faultString.split('\n')[-2] + e.faultString.split('\n')[-1]
        return jsonify(status=code, message={"error_message": error_message, }), 500
    except Exception as e:
        code, error_message = e.args
        return jsonify(status=code, message={"error_message": error_message, }), 500
    return jsonify(status=200, message={'uid': uid, }), 200


@bp.route('/create-portal-user', methods=["POST", ])
def create_portal_user():
    try:
        uid = odoo_create_portal_user(request.get_json())
    except Fault as e:
        code, error_message = e.faultCode, e.faultString.split('\n')[-2] + e.faultString.split('\n')[-1]
        return jsonify(status=code, message={"error_message": error_message, }), 500
    except Exception as e:
        code, error_message = e.args
        return jsonify(status=code, message={"error_message": error_message, }), 500
    return jsonify(status=200, message={'uid': uid, }), 200
