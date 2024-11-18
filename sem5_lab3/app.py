

from flask import Flask, render_template, session, json, redirect,url_for
from query.route import blueprint_query
from auth.route import blueprint_auth
from report.route import blueprint_report

from database.sql_provider import SQLProvider


app = Flask(__name__)
with open("../data/dbconfig.json") as f:
    app.config['db_config'] = json.load(f)

with open("../data/db_access.json") as f:
    app.config['db_access'] = json.load(f)


app.secret_key = 'You will never guess'

app.register_blueprint(blueprint_query, url_prefix='/query')
app.register_blueprint(blueprint_auth, url_prefix='/auth')
app.register_blueprint(blueprint_report, url_prefix='/report')

@app.route('/')
def main_menu():
    user_role = "unauth"
    if 'user_group' in session:
        user_role = session.get('user_group')
        message = f'Вы авторизованы как {user_role}'
    else:
        message = 'Вам необходимо авторизоваться'

    return render_template('main_menu.html', message=message, role=user_role)

@app.route('/exit')
def exit_func():
    if 'user_group' in session:
        session.clear()
        return render_template('logout.html')
    return redirect(url_for('main_menu'))

@app.route('/error')
def error_message():
    return render_template("error.html", message="Какая-то ошибка :(")

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5001, debug=True)
