
import json
from flask import Flask, render_template, Blueprint, current_app
from access import group_required

from database.select import select_list
from database.select import select_dict

blueprint_query = Blueprint('query_bp', __name__, template_folder='templates')


@blueprint_query.route('/')
#неявное обращение к декоратору
@group_required
def query_index():
    prod_category = 1
    _sql = f""" SELECT prod_id, prod_name, prod_measure, prod_price, prod_category FROM product
                WHERE prod_category = {prod_category}"""
    result = select_dict(current_app.config['db_config'], _sql)
    if result:
        prod_title = 'Результаты из БД'
        return render_template("dynamic.html", prod_title=prod_title, products=result)
    else:
        return "No result"


