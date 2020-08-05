from flask import Flask


def create_app():
    app = Flask(__name__, )

    @app.route("/")
    def check():
        return "server is running..."

    return app
