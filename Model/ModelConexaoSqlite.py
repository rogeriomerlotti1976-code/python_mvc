import pyodbc

from Model.DAO.Interface.ModelConexaoInterface import IModelConexao

class ModelConexaoSqlite(IModelConexao):
    def __init__(self, database: str):
        self.__database = database

    def conectar(self):
        dados_conexao = ("""
            Driver={{SQLite3 ODBC Driver}};
            Server=localhost;
            Database={};
            """.format(self.__database)
        )

        conexao = pyodbc.connect(dados_conexao)
        return conexao