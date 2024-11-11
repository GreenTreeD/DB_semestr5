from dataclasses import dataclass
from database.select import select_list

@dataclass
class ProductInfoRespronse:
    result: tuple
    error_message: str
    status: bool

def model_route(db_config, user_input_data, sql_provider):
    error_message = ''
    if 'prod_category' not in user_input_data:
        print("user_input_data=", user_input_data)
        result = ()
        return ProductInfoRespronse(result, error_message=error_message, status=False)
    _sql = sql_provider.get('product.sql', prod_category = user_input_data['prod_category'])
    #print("sql=", _sql)
    result, schema = select_list(db_config, _sql)
    if result or schema:
        return ProductInfoRespronse(result, error_message=error_message, status=True)
    return ProductInfoRespronse(result, error_message=error_message, status=False)