from Model.ModelConexaoSqlite import  ModelConexaoSqlite
from Model.ModelConexaoMySQL import ModelConexaoMySQL
from Enums.Enums import Banco
from Model.DAO.Interface.ModelConexaoInterface import IModelConexao
from Utils.SistemaUtils import SistemaUtils
from configparser import ConfigParser

class ModelConexaoFactory():
    @staticmethod
    def criar() -> IModelConexao:
        nome_arquivo_config = SistemaUtils.get_nome_arquivo_config()
        config = ConfigParser()
        config.read(nome_arquivo_config)
        tipo_banco = Banco(config["DATABASE"]["TIPO"].upper())

        match tipo_banco:
            case Banco.Sqlite:
                return ModelConexaoSqlite(config["SQLITE"]["DATABASE"])
            case Banco.MySQL:
                return ModelConexaoMySQL(config["MYSQL"]["HOST"],
                                         config["MYSQL"]["PORT"],
                                         config["MYSQL"]["DATABASE"],
                                         config["MYSQL"]["USER"],
                                         config["MYSQL"]["PASSWORD"])
            case _:
                return None