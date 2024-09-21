from flask import Flask, render_template
from pymysql import connect


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world from Flask!"

@app.route("/static")
def static_index():
    return render_template("static.html")

@app.route("/dynamic")
def dynamic_index():
    prod_title = "Товары мясного отдела"
    products =  [
        {'prod_name' : 'Говядина', 'prod_measure' : 'кг', 'prod_price' : 900},
        {'prod_name': 'Свинина', 'prod_measure': 'кг', 'prod_price': 700},
        {'prod_name': 'Кролик', 'prod_measure': 'кг', 'prod_price': 1200},
        {'prod_name': 'Курица', 'prod_measure': 'кг', 'prod_price': 400},
        {'prod_name': 'Ножки курицы', 'prod_measure': 'шт', 'prod_price': 500},
        {'prod_name': 'Филе кролика', 'prod_measure': 'шт', 'prod_price': 1000},
        {'prod_name': 'Бараньи рёбрышки', 'prod_measure': 'шт', 'prod_price': 1200}
    ]
    return render_template("dynamic.html", prod_title=prod_title, products=products)

@app.route("/product")
def product_index():
    try:
        conn = connect(host='127.0.0.1', user='root', password='root', database='supermarket')
        cursor = conn.cursor()
        return "Успешно."
    except OperationalError as err:
        print(err.args)
        return "Ошибка подключения."



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)


