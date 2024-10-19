

from flask import Blueprint, session, redirect, url_for


blueprint_auth = Blueprint('auth_bp', __name__, template_folder='templates')



@blueprint_auth.route('/')
def auth_index():
    user_group = 'admin'
    user_id = 1
    session['user_group'] = user_group
    session['user_id'] = user_id
    # Заносим в сессию, чтобы все остальные страницы не требовали аутентификацию, т.к. HTTP не помнит, что вы заходили
    # Ко второй лабе доделать заглушку
    print('Выполнена аутентификация')
    return redirect(url_for('main_menu'))
