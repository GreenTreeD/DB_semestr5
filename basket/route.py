# Первоначальная версия данного файла без кэширования, оставлена на всякий случай
#
# from flask import Blueprint, session, redirect, url_for, render_template, current_app, request
# from database.sql_provider import SQLProvider
# import os
# from basket.model_route import model_route_all_goods
#
#
#
# blueprint_basket = Blueprint('basket_bp', __name__, template_folder='templates')
#
# provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))
#
# @blueprint_basket.route('/', methods=['GET'])
# def basket_index():
#     if 'basket' in session:
#         basket = session['basket']
#     else:
#         basket = None
#
#     goods = model_route_all_goods(current_app.config['db_config'], provider)
#
#     if goods.result == False:
#         return render_template('error.html', message='Ошибка сервера, товары не найдены')
#
#     return render_template('basket_dynamic.html', goods=goods, basket=basket)
#
# @blueprint_basket.route('/', methods=['GET'])
# def basket_add():
#     user_data = request.form
#     res_info = model_route_add_basket(current_app.config['db_config'], user_data, provider)
#     info = res_info.result
#     if 'basket' in session:
#         basket = session['basket']
#         amount = session['basket'][info['prod_id']]['amount'] + 1
#     else:
#         basket = None
#         amount = 1
#
#     session['basket'][info['prod_id']] = {
#         'prod_name' : info['prod_name'],
#         'prod_price': info['prod_price'],
#         'amount' : amount}
#     if res_info.status == False:
#         session.pop('basket')
#         return render_template('error.html', message="Товар не добавлен, ошибка сервера")
#
#     render_template('basket_dynamic.html', goods=goods, basket=basket)
#
#
# @blueprint_basket.route('/clear_basket')
# def clear_basket():
#     pass
#
# @blueprint_basket.route('/save_order')
# def save_order():
#     pass
