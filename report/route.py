

from flask import Blueprint, session, redirect, url_for, render_template, current_app, request
from access import group_required
from database.sql_provider import SQLProvider
from report.model_route import model_route, model_route_create
import os
from datetime import datetime


blueprint_report = Blueprint('report_bp', __name__, template_folder='templates')

provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@blueprint_report.route('/', methods=['GET'])
@group_required
def report_index():
    return render_template('report_static.html',
                           date_value=f"{datetime.now().year}-{datetime.now().month}",
                           user_access = (session.get("user_group") == "manager"))


@blueprint_report.route('/', methods=['POST'])
@group_required
def report_main():
    user_data = request.form
    if user_data.get('yearmonth'):
        date = user_data.get('yearmonth')
        res_info = model_route(current_app.config['db_config'], user_data, provider)
        return render_template('report_dynamic.html', status=res_info.status,
                               products=res_info.result,
                               date_value=date,
                               message=res_info.error_message)
    else:
        res_info = model_route_create(current_app.config['db_config'], user_data, provider)
        if res_info.result:
            return redirect(url_for('bp_report.report_main'))
        else:
            return render_template("error.html", message=res_info.error_message)

