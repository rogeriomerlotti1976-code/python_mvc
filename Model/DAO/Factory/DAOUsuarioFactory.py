from Model.DAO.Interface.ModelConexaoInterface import IModelConexao
from Model.DAO.Sqlite.DAOUsuarioSqlite import DAOUsuarioSqlite
from Model.DAO.MySql.DAOUsuarioMySql import DAOUsuarioMySql
from Model.DAO.Interface.DAOUsuarioInterfaces import IUsuarioDAO
from Enums.Enums import Banco

class DAOUsuarioFactory():
    @staticmethod
    def criar(banco: Banco, conexao: IModelConexao) -> IUsuarioDAO:
        match banco:
            case Banco.Sqlite:
                return DAOUsuarioSqlite(conexao)
            case Banco.MySQL:
                return DAOUsuarioMySql(conexao)
            case _:
                raise ValueError(f"DAO não implementado para: {banco.value}")