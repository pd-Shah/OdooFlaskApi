from xmlrpc.client import ServerProxy
from flask import current_app


def get_version():
    base_url = current_app.config['url']
    common = ServerProxy('{}/xmlrpc/2/common'.format(base_url))
    return common.version()
