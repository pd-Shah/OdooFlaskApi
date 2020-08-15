from flask import (
    Blueprint,
    jsonify,
)

bp = Blueprint(
    "error",
    __name__,
    url_prefix="/error"
)


@bp.app_errorhandler(400)
def error_400(**kwargs):
    msg = "Things Break Sometimes. What did you expect!?"
    code = 400
    return jsonify(status=code, message={'error': msg, }), code
