

from flask import Blueprint, session, redirect, url_for, render_template, current_app, request
from database.sql_provider import SQLProvider
import os
from auth.model_route import model_route_auth_req, model_route_reg_exist_check, model_route_reg_new
import hashlib


blueprint_auth = Blueprint('auth_bp', __name__, template_folder='templates')

provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))

@blueprint_auth.route('/', methods=['GET'])
def auth_index():
    return render_template('static.html')


@blueprint_auth.route('/', methods=['POST'])
def auth_main():
    user_data = request.form
    res_info = model_route_auth_req(current_app.config['db_config'], user_data, provider)
    print(res_info)
    if not res_info.status:
        return "Ошибка"
    if not res_info.result:
        return "Ошибка"

    user_group = res_info.result[0][2]
    session['user_group'] = user_group
    session['user_id'] = hashlib.sha256(b"{res_info.result[0][0]}").hexdigest()
    # Заносим в сессию, чтобы все остальные страницы не требовали аутентификацию, т.к. HTTP не помнит, что вы заходили
    # Ко второй лабе доделать заглушку
    print('Выполнена аутентификация')
    return redirect(url_for('main_menu'))

@blueprint_auth.route('/registration', methods=['GET'])
def registration_index():
    return render_template('reg.html')

@blueprint_auth.route('/registration', methods=['POST'])
def registration_main():
    user_data = request.form
    if user_data['password'] != user_data['password1']:
        return "Пароли не совпадают"
    res_info = model_route_reg_exist_check(current_app.config['db_config'], user_data, provider)
    print(res_info)
    if not res_info.status:
        return "Ошибка"
    if res_info.result:
        return "Такой пользователь уже существует"

    res_info = model_route_reg_new(current_app.config['db_config'], user_data, provider)
    if not res_info.status:
        return "Ошибка"

    print("Регистрация успешна")

    return redirect(url_for('auth_bp.auth_index'))
