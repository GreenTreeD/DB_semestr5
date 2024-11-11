
import os
from flask import render_template, Blueprint, current_app, request
from access import group_required
from model_route import model_route
from database.sql_provider import SQLProvider


blueprint_query = Blueprint('query_bp', __name__, template_folder='templates')

provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))

@blueprint_query.route('/', methods=['GET'])
# неявное обращение к декоратору
@group_required
def query_index():
    return render_template("input_category.html")

@blueprint_query.route('/', methods=['POST'])
@group_required
def product_result_handler():
    user_data = request.form
    print("User data: ", user_data)
    res_info = model_route(current_app.config['db_config'], user_data, provider)
    print("res_info.result = ", res_info.result)
    if res_info.status:
        if res_info.result:
            prod_title = 'Результаты из БД'
            return render_template("dynamic.html", prod_title=prod_title, products=res_info.result)
        return render_template('error.html', message="Нет результатов")
    else:
        return render_template('error.html', message="Ошибка сервера")




