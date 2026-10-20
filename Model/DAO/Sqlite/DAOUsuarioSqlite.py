from pandas.core.interchange import column

from Model.DAO.Interface.DAOUsuarioInterfaces import IUsuarioDAO
from Model.Entity.EntityUsuario import EntityUsuario
from Model.DAO.Interface.ModelConexaoInterface import IModelConexao
from Model.DAO.Sqlite.SqliteUtils import SqliteUtils

class DAOUsuarioSqlite(IUsuarioDAO):
    def __init__(self, conexao: IModelConexao):
        self.__conexao = conexao

    def inserir(self, usuario: IEntityUsuario) -> int:
        sql = (f'INSERT INTO USUARIO(NOME, LOGIN, SENHA) VALUES ("{usuario.nome}", '
               f'"{usuario.login}", "{usuario.senha}")')

        try:
            try:
                conexao = self.__conexao.conectar()
                cursor = conexao.cursor()
                cursor.execute(sql)
                usuario.id = SqliteUtils.get_id(cursor)
                conexao.commit()
                return usuario.id
            except Exception as e:
                raise ValueError(f'Erro na inclusão do usuário: {e}')
        finally:
            cursor.close()
            conexao.close()

    def atualizar(self, usuario: IEntityUsuario):
        sql = (f'UPDATE USUARIO SET NOME = "{usuario.nome}", '
               f'LOGIN = "{usuario.login}" '
               f'WHERE ID_USUARIO = {usuario.id}')
        try:
            try:
                conexao = self.__conexao.conectar()
                cursor = conexao.cursor()
                cursor.execute(sql)
                conexao.commit()
            except Exception as e:
                raise ValueError(f'Erro na atualização do usuário: {e}')
        finally:
            cursor.close()
            conexao.close()

    def excluir(self, id: int):
        sql = f'UPDATE USUARIO SET ATIVO = 0 WHERE ID_USUARIO = {id}'
        try:
            try:
                conexao = self.__conexao.conectar()
                cursor = conexao.cursor()
                cursor.execute(sql)
                conexao.commit()
            except Exception as e:
                conexao.rollback()
                raise ValueError(f'Erro ao excluir o usuário: {e}')
        finally:
            cursor.close()
            conexao.close()

    def consultar_por_id(self, id: int) -> IEntityUsuario:
        sql = f'SELECT ID_USUARIO, NOME, LOGIN, SENHA FROM USUARIO WHERE ID_USUARIO = {id}'
        try:
            try:
                conexao = self.__conexao.conectar()
                cursor = conexao.cursor()
                cursor.execute(sql)
                registro = cursor.fetchone()

                if registro is None:
                    return None

                usuario = EntityUsuario()
                usuario.id = registro[0]
                usuario.nome = registro[1]
                usuario.login = registro[2]
                usuario.senha = registro[3]
                return usuario
            except Exception as e:
                raise ValueError(f'Erro ao consultar o usuário por ID: {e}')
        finally:
            cursor.close()
            conexao.close()

    def consultar_por_login(self, login: str) -> IEntityUsuario:
        pass

    def existe(self, login: str) -> bool:
        sql = f'SELECT EXISTS(SELECT 1 FROM USUARIO WHERE LOGIN = "{login}") AS EXISTE'
        try:
            try:
                conexao = self.__conexao.conectar()
                cursor = conexao.cursor()
                cursor.execute(sql)
                return bool(cursor.fetchone()[0])
            except Exception as e:
                raise ValueError(f'Erro ao verificar se o login existe: {e}')
        finally:
            cursor.close()
            conexao.close()

    def listar_tudo(self) -> "tuple[list, list]":
        sql = 'SELECT ID_USUARIO, NOME, LOGIN FROM USUARIO WHERE ATIVO = 1'
        try:
            try:
                conexao = self.__conexao.conectar()
                cursor = conexao.cursor()
                cursor.execute(sql)
                colunas = [coluna[0] for coluna in cursor.description]
                registros = cursor.fetchall()
                return colunas, registros
            except Exception as e:
                raise ValueError(f'Erro ao listar todos os usuários: {e}')
        finally:
            cursor.close()
            conexao.close()

    def autenticar(self, login: str, senha: str) -> bool:
        sql = f'SELECT * FROM USUARIO WHERE LOGIN = "{login}" AND SENHA = "{senha}" AND ATIVO = 1'

        try:
            try:
                conexao = self.__conexao.conectar()
                cursor = conexao.cursor()
                cursor.execute(sql)
                return bool(cursor.fetchone()[0])
            except Exception as e:
                raise ValueError(f'Erro na autenticação do usuário: {e}')
        finally:
            cursor.close()
            conexao.close()


    def pesquisar(self, texto: str) -> "tuple[list, list]":
        sql = ('SELECT ID_USUARIO, NOME, LOGIN '
               'FROM USUARIO '
               f'WHERE (NOME LIKE "%{texto}%" '
               f'OR LOGIN LIKE "%{texto}%") '
               'AND ATIVO = 1')

        try:
            try:
                conexao = self.__conexao.conectar()
                cursor = conexao.cursor()
                cursor.execute(sql)
                colunas = [coluna[0] for coluna in cursor.description]
                registros = cursor.fetchall()
                return colunas, registros
            except Exception as e:
                raise ValueError(f'Erro ao pesquisar usuários: {e}')
        finally:
            cursor.close()
            conexao.close()