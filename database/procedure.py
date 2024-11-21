from database.DBcm import DBContextManager
from pymysql.err import OperationalError
from pymysql.err import ProgrammingError


def call_proc (db_config: dict, proc_name: str, params : tuple):
    res = []
    with DBContextManager(db_config) as cursor:
        if cursor is None:
            raise ValueError('Cursor not created')
        try:
            res = cursor.callproc(proc_name, params)
        except ProgrammingError as err:
            print("error in procedure.py:",err)
        except OperationalError as err:
            print("error in procedure.py:",err)
    return res

