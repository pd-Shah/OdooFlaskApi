from xmlrpc.client import ServerProxy
from flask import current_app, session
from .schemas import PortalUser, LoginUser


def odoo_version(endpoint='{}/xmlrpc/2/common', ):
    base_url = current_app.config['O_URL']
    common = ServerProxy(endpoint.format(base_url))
    return common.version()


def odoo_login(user, endpoint='{}/xmlrpc/2/common', ):
    session.pop('username', None)
    session.pop('password', None)
    login_user = LoginUser()
    login_user = login_user.load(user)
    session['username'] = login_user['username']
    session['password'] = login_user['password']
    base_url = current_app.config['O_URL']
    common = ServerProxy(endpoint.format(base_url))
    uid = common.authenticate(
        current_app.config['O_DB'],
        session['username'],
        session['password'],
        {}, )
    session['uid'] = uid
    return uid


def odoo_create_portal_user(user_obj, endpoint='{}/xmlrpc/2/object', ):
    portal_user = PortalUser()
    user_obj = portal_user.load(user_obj)
    user_obj["mobile"] = user_obj['country_code'].replace("+", "00") + user_obj['phone_number']
    base_url = current_app.config['O_URL']
    models = ServerProxy(endpoint.format(base_url))
    id = models.execute_kw(
        current_app.config['O_DB'],
        session['uid'],
        session['password'],
        'integrated_user',
        'create',
        [user_obj], )
    return id
