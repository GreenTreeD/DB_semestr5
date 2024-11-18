from dataclasses import dataclass
from database.select import select_list
from datetime import date
from database.insert import insert_one


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
            return ProductInfoRespronse(tuple(), error_message="Заказ не был создан", status=False)

    result = tuple(order_id)
    return ProductInfoRespronse(result, error_message="", status=True)





