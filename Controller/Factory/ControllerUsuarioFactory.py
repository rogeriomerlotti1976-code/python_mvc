from configparser import ConfigParser
from Enums.Enums import Banco
from Model.Factory.ModelConexaoFactory import ModelConexaoFactory
from Model.DAO.Factory.DAOUsuarioFactory import DAOUsuarioFactory
from Model.ModelUsuario import ModelUsuario
from Controller.Interface.IControllerUsuario import IControllerUsuario
from Controller.ControllerUsuario import ControllerUsuario
from Utils.SistemaUtils import SistemaUtils

class ControllerUsuarioFactory():
    @staticmethod
    def criar() -> ControllerUsuario:
        arquivo_config = SistemaUtils.get_nome_arquivo_config()
        config = ConfigParser()
        config.read(arquivo_config)
        conexao = ModelConexaoFactory.criar()
        banco = Banco(config["DATABASE"]["TIPO"].upper())
        dao = DAOUsuarioFactory.criar(banco, conexao)
        model = ModelUsuario(dao)
        controller = ControllerUsuario(model)
        return controller