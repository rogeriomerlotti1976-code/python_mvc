from enum import Enum

class Banco(Enum):
    Sqlite = 'SQLITE'
    MySQL = 'MYSQL'
    Postgres = 'POSTGRES'