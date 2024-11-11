

from functools import wraps
from flask import session, request, redirect, url_for, current_app

def login_required(func):
    @wraps(func)
    def wrapper(*argc, **kwargs):
        if 'user_group' in session:
            return func(*argc, **kwargs)
        else:
            return redirect(url_for('main_menu'))

    return wrapper

def group_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user_group' in session:
            user_role = session.get('user_group')
            user_request = request.endpoint
            print('request_endpoint=', user_request)
            user_bp = user_request.split('.')[0]
            access = current_app.config['db_access']
            if user_role in access and user_bp in access[user_role]:
                return func(*args, **kwargs)
            else:
                return redirect(url_for('main_menu'))
        else:
            return redirect(url_for('main_menu'))
    return wrapper
