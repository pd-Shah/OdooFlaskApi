from xmlrpc.client import ServerProxy
from flask import current_app
from .schemas import PortalUser


def odoo_version(endpoint='{}/xmlrpc/2/common', ):
    base_url = current_app.config['O_URL']
    common = ServerProxy(endpoint.format(base_url))
    return common.version()


def odoo_login(endpoint='{}/xmlrpc/2/common', ):
    base_url = current_app.config['O_URL']
    common = ServerProxy(endpoint.format(base_url))
    uid = common.authenticate(
        current_app.config['O_DB'],
        current_app.config['O_USERNAME'],
        current_app.config['O_PASSWORD'],
        {}, )
    current_app.config['O_UID'] = uid
    return uid


def odoo_create_portal_user(user_obj, endpoint='{}/xmlrpc/2/object', ):
    portal_user = PortalUser()
    user_obj = portal_user.dump(user_obj)
    base_url = current_app.config['O_URL']
    models = ServerProxy(endpoint.format(base_url))
    id = models.execute_kw(
        current_app.config['O_DB'],
        current_app.config['O_UID'],
        current_app.config['O_PASSWORD'],
        'integrated_user',
        'create',
        [user_obj], )
    return id
