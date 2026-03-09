
from flask import Flask, render_template, session, json, redirect,url_for
from auth.route import blueprint_auth

app = Flask(__name__)
with open("data/dbconfig.json") as f:
    app.config['db_config'] = json.load(f)

with open("data/db_access.json") as f:
    app.config['db_access'] = json.load(f)

# with open("../data/cache_config.json") as f:
#     app.config['cache_config'] = json.load(f)


app.register_blueprint(blueprint_auth, url_prefix='/auth')

app.secret_key = 'You will never guess'

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

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', message="404 Not Found. Данной страницы не существует."), 404


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5001, debug=True)