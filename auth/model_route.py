from dataclasses import dataclass
from database.select import select_string

@dataclass
class ProductInfoRespronse:
    result: tuple
    error_message: str
    status: bool


def model_route_auth_req(db_config, user_input_data, sql_provider):
    error_message = ''
    _sql = sql_provider.get('users.sql', e_login = user_input_data['login'], e_password=user_input_data['password'])
    result, schema = select_string(db_config, _sql)
    if result or schema:
        return ProductInfoRespronse(result, error_message=error_message, status=True)
    return ProductInfoRespronse(result, error_message=error_message, status=False)

def model_route_reg_exist_check(db_config, user_input_data, sql_provider):
    error_message = ''
    _sql = sql_provider.get('users_check.sql', e_login = user_input_data['login'])
    result, schema = select_string(db_config, _sql)
    if result or schema:
        return ProductInfoRespronse(result, error_message=error_message, status=True)
    return ProductInfoRespronse(result, error_message=error_message, status=False)

def model_route_reg_new(db_config, user_input_data, sql_provider):
    error_message = ''
    _sql = sql_provider.get('users_new.sql',
                            e_login=user_input_data['login'],
                            e_password=user_input_data['password'],
                            e_role='user')
    result = select_string(db_config, _sql)
    if result:
        return ProductInfoRespronse(tuple(), error_message=error_message, status=True)
    return ProductInfoRespronse(tuple(), error_message=error_message, status=False)