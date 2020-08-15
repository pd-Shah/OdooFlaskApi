from xmlrpc.client import Fault
from functools import wraps
from flask import (
    Blueprint,
    jsonify,
)

bp = Blueprint(
    "error",
    __name__,
    url_prefix="/error"
)


def error_check(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            result = f(*args, **kwargs)
        except Fault as e:
            code, error_message = e.faultCode, e.faultString.split('\n')[-2] + e.faultString.split('\n')[-1]
            return jsonify(status=code, message={"error_message": error_message, }), 500
        except Exception as e:
            error_message = e.args
            return jsonify(status=500, message={"error_message": error_message, }), 500
        return result

    return decorated_function
