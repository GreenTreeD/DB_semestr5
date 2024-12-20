from database.DBcm import DBContextManager
from pymysql.err import OperationalError


def delete(db_config: dict, _sql: str):
    with DBContextManager(db_config) as cursor:
        if cursor is None:
            raise ValueError("Cursor not created")
        else:
            try:
                cursor.execute(_sql)
            except OperationalError as error:
                print("delete error: ", error)
                return False
            else:
                print("Cursor no errors")
    return True