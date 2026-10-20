from pyodbc import Cursor

class SqliteUtils():
    @staticmethod
    def get_id(cursor: Cursor) -> int:
        cursor.execute('SELECT last_insert_rowid()')
        return cursor.fetchone()[0]