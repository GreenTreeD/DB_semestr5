from database.DBcm import DBContextManager
from pymysql.err import OperationalError
from pymysql.err import Error


def insert_one(db_config: dict, _sql: str):
    with DBContextManager(db_config) as cursor:
        if cursor is None:
            raise ValueError("Cursor not created")
        else:
            try:
                cursor.execute(_sql)
            except Error as error:
                print("insert_one error: ", error)
                return False
            else:
                print("Cursor no errors")
    return True