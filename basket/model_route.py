from dataclasses import dataclass
from database.select import select_list
from datetime import date
from database.insert import insert_one
from database.delete import delete
from database.DBcm import DBContextManager
from pymysql import Error


@dataclass
class ProductInfoRespronse:
    result: tuple
    error_message: str
    status: bool


def model_route_transaction_order(db_config : dict, sql_provider, basket : dict, user_id: int):
    ddate = date.today()
    _sql = sql_provider.get('create_order.sql', e_user_id = user_id, e_order_date = ddate)
    print(_sql)
    result = insert_one(db_config, _sql)
    if not result:
        return ProductInfoRespronse(tuple(), error_message="Заказ не был создан", status=False)
    _sql = sql_provider.get('get_order.sql', e_user_id=user_id, e_order_date=ddate)
    order_id = select_list(db_config,_sql)[0][0]
    print(basket)
    for key, value in basket.items():
        _sql = sql_provider.get('insert_order_product.sql',
                                e_order_id = order_id[0],
                                e_prod_id = int(key),
                                e_amount = int(value))
        print(_sql)
        result = insert_one(db_config, _sql)
        if not result:
            _sql = sql_provider.get('delete_order.sql', delid = order_id)
            delete(db_config, _sql)
            _sql = sql_provider.get('delete_orders.sql', delid=order_id)
            delete(db_config, _sql)
    result = tuple(order_id)
    return ProductInfoRespronse(result, error_message="", status=True)


def transaction_order(db_config : dict, sql_provider, basket : dict, user_id: int):
    ddate = date.today()
    order_id = None
    try:
        with DBContextManager(db_config) as cursor:
            # пупупу пупупу автоинкремент прибавляется но не вычитается при ошибке
            # любая ошибка при ходе выполнения интерпретируется как выход из курсора, см DBContextManager.__exit__
            _sql = sql_provider.get('create_order.sql', e_user_id=user_id, e_order_date=ddate)
            try:
                cursor.execute(_sql)
                print("success :", _sql)
            except Error as err:
                print("error in transaction_order():", err.args)
                return ProductInfoRespronse(tuple(), error_message="Заказ не был создан", status=False)
            try:
                order_id = cursor.lastrowid
            except AttributeError as err:
                print("attr error")
                return ProductInfoRespronse(tuple(), error_message="Заказ не был создан", status=False)

            print(order_id)
            print(basket.items())
            for key, value in basket.items():
                _sql = sql_provider.get('insert_order_product.sql',
                                        e_order_id=order_id,
                                        e_prod_id=int(key),
                                        e_amount=int(value))
                try:
                    cursor.execute(_sql)
                    print("success :", _sql)
                except Error as err:
                    print("error in transaction_order():", err.args)
                    return ProductInfoRespronse(tuple(), error_message="Заказ не был создан", status=False)

        result = [order_id] if order_id else None
        return ProductInfoRespronse(result, error_message="", status=True)
    except Error as err:
        print("error in transaction_order():", err.args)
        return ProductInfoRespronse(tuple(), error_message="Заказ не был создан", status=False)

















