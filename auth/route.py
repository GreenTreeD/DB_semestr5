

from flask import Blueprint, session, redirect, url_for, render_template, current_app, request
from database.sql_provider import SQLProvider
import os
from auth.model_route import model_route_auth_req, model_route_reg_exist_check, model_route_reg_new
import hashlib


blueprint_auth = Blueprint('auth_bp', __name__, template_folder='templates')

provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))

@blueprint_auth.route('/', methods=['GET'])
def auth_index():
    if 'user_group' in session:
        session.clear()
    return render_template('static.html')


@blueprint_auth.route('/', methods=['POST'])
def auth_main():
    user_data = request.form
    res_info = model_route_auth_req(current_app.config['db_config'], user_data, provider)
    print(res_info)
    if not res_info.status:
        return render_template('error_auth.html', message="Ошибка сервера")
    if not res_info.result:
        return render_template('error_auth.html', message="Такой пользователь не существует")

    session['user_group'] = res_info.result[0][3]
    session['user_id'] = res_info.result[0][0]
    # Заносим в сессию, чтобы все остальные страницы не требовали аутентификацию, т.к. HTTP не помнит, что вы заходили
    # Ко второй лабе доделать заглушку
    print('Выполнена аутентификация')
    return redirect(url_for('main_menu'))

@blueprint_auth.route('/registration', methods=['GET'])
def registration_index():
    return render_template('reg.html')

@blueprint_auth.route('/registration', methods=['POST'])
def registration_main():
    if 'user_group' in session:
        session.clear()
    user_data = request.form
    if user_data['password'] != user_data['password1']:
        return render_template('error.html', message= "Пароли не совпадают")
    if 'user_id' in session:
        return render_template('error.html', message="Вы не вышли из учётной записи")

    res_info = model_route_reg_exist_check(current_app.config['db_config'], user_data, provider)
    print(res_info)
    if not res_info.status:
        return render_template('error.html', message="Ошибка сервера")
    if res_info.result:
        return render_template('error.html', message="Такой пользователь уже существует")

    res_info = model_route_reg_new(current_app.config['db_config'], user_data, provider)
    if not res_info.status:
        return render_template('error.html', message="Ошибка сервера")

    print("Регистрация успешна")

    return redirect(url_for('auth_bp.auth_index'))
