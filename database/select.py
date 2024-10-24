
# функции связанные с выполнением запроса в базу данных

from database.DBcm import DBContextManager
from pymysql.err import OperationalError


def select_list(db_config: dict, _sql: str):

    # порядок работы конструкции with
    # инициируются переменные (cursor) в методе __init__
    # управление передаётся методу __enter__
    # создаётся курсор или ничего, все дела
    # возвращение управления вызвавшей функции
    # если курсор не был создан, то создаётся ошибка ValueError
    # выполняются все действия в функции, если возникает ошибка, то вызывается метод __error__
    # вот такая вот передача управления в неявном виде...

    result = ()
    schema = []
    with DBContextManager(db_config) as cursor:

        if cursor is None:
            raise ValueError("Cursor not created")
        else:
            try:
                cursor.execute(_sql)
                result = cursor.fetchall()
            except OperationalError as error:
                print("error: ", error)
                return result, schema
            else:
                print("Cursor no errors")
            # print(cursor.description)
            # в cursor.description[0] лежат имена полей из таблицы

            schema = [item[0] for item in cursor.description]

    return result, schema

def select_dict(db_config: dict, _sql: str):
    result, schema = select_list(db_config, _sql)
    result_dict = []
    for item in result:
        result_dict.append(dict(zip(schema, item)))
    # print(result_dict)
    return result_dict


def select_string(db_config: dict, _sql: str):
    result = dict()
    schema = list()
    print(_sql)

    with DBContextManager(db_config) as cursor:

        if cursor is None:
            raise ValueError("Cursor not created")
        else:
            try:
                cursor.execute(_sql)
                result = cursor.fetchall()
            except OperationalError as error:
                print("error: ", error)
                return result
            else:
                print("Cursor no errors")

            schema = [item[0] for item in cursor.description]

    return result, schema





