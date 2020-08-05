from flask import Flask
from app.packages import auth
from settings import config


def create_app():
    app = Flask(__name__, )
    app.config.from_object(config)
    app.register_blueprint(auth.bp, url_prefix='/api/v1')

    @app.route("/")
    def check():
        import xmlrpc.client
        info = xmlrpc.client.ServerProxy('https://demo.odoo.com/start').start()
        app.config['url'] = info['host']
        app.config['db'] = info['database']
        app.config['username'] = info['user']
        app.config['password'] = info['password']
        return "server is running..."

    return app
