from Model.DAO.Interface.DAOUsuarioInterfaces import IUsuarioDAO
from Model.DAO.Interface.ModelConexaoInterface import IModelConexao
from Model.Entity.EntityUsuario import EntityUsuario

class DAOUsuarioMySql(IUsuarioDAO):
    def __init__(self, conexao: IModelConexao):
        self__conexao = conexao

    def inserir(self, usuario: EntityUsuario) -> int:
        sql = f'INSERT INTO USUARIO(LOGIN, SENHA) VALUES ("{usuario.login}", "{usuario.senha}")'

        try:
            try:
                conexao = self.__conexao.conectar()
                cursor = conexao.cursor()
                cursor.execute(sql)
                cursor.execute('SELECT last_insert_rowid()')
                usuario.id = SqliteUtils.get_id(cursor)
                conexao.commit()
                return usuario.id
            except Exception as e:
                raise ValueError(f'Erro na inclusão do usuário: {e}')
        finally:
            conexao.close()

    def atualizar(self, usuario: EntityUsuario) -> bool:
        pass

    def excluir(self, id: int) -> EntityUsuario:
        pass

    def consultar_por_id(self, id: int) -> EntityUsuario:
        pass

    def consultar_por_login(self, login: str) -> EntityUsuario:
        pass

    def existe(self, login: str)-> bool:
        pass
