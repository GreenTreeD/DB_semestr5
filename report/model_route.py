from dataclasses import dataclass
from database.select import select_list

@dataclass
class ProductInfoRespronse:
    result: tuple
    error_message: str
    status: bool


def model_route(db_config, user_input_data, sql_provider):
    date = user_input_data.get('yearmonth').split('-')
    _sql = sql_provider.get('get_report.sql', e_year=date[0], e_month=date[1])
    result, schema = select_list(db_config, _sql)
    if result:
        return ProductInfoRespronse(result, error_message="", status=True)
    return ProductInfoRespronse(result, error_message="На данную дату отчёт отсутствует", status=False)

