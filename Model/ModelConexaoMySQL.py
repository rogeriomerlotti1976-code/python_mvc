import mysql.connector
from Model.DAO.Interface.ModelConexaoInterface import IModelConexao

class ModelConexaoMySQL(IModelConexao):
    def __init__(self, host, port, database, user, password: str):
        self.__host = host
        self.__port = port
        self.__database = database
        self.__user = user
        self.__password = password

    def conectar(self):
        dados_conexao = ("""
            host={},
            port={},
            database={},
            user={},
            password={}
        """.format(self.host, self.__port, self.__database, self.__user, self.__password))

        conexao = mysql.connector.connect(dados_conexao)
        return conexao