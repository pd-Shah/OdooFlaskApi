from flask import Flask
from app.packages import auth, error
from settings import config


def create_app():
    app = Flask(__name__, )
    app.config.from_object(config)
    app.register_blueprint(auth.bp, url_prefix='/api/v1')
    # app.register_blueprint(error.bp, )

    @app.route("/")
    def check():
        return "server is running..."

    return app
