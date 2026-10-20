from Model.DAO.Interface.DAOUsuarioInterfaces import IUsuarioDAO
from Model.Interface.IModelUsuario import IModelUsuario
from Model.Entity.EntityUsuarioInterface import IEntityUsuario

class ModelUsuario(IModelUsuario):
    def __init__(self, dao_usuario: IUsuarioDAO):
        self.__dao_usuario = dao_usuario

    def inserir(self, usuario: IEntityUsuario) -> int:
        if ModelUsuario.existe(self, usuario.login):
            raise ValueError('Login já cadastrado. Verifique.')

        return self.__dao_usuario.inserir(usuario)

    def atualizar(self, usuario: IEntityUsuario):
        return self.__dao_usuario.atualizar(usuario)

    def excluir(self, id: int):
        return self.__dao_usuario.excluir(id)

    def consultar_por_id(self, id: int) -> list:
        return self.__dao_usuario.consultar_por_id(id)

    def consultar_por_login(self, login: str) -> IEntityUsuario:
        raise ValueError('método ModelUsuario.consultar_por_login não implementado')

    def existe(self, login: str) -> bool:
        return self.__dao_usuario.existe(login)

    def listar_tudo(self) -> "tuple[list, list]":
        return self.__dao_usuario.listar_tudo()

    def autenticar(self, login: str, senha: str) -> bool:
        return self.__dao_usuario.autenticar(login, senha)

    def pesquisar(self, texto: str) -> "tuple[list, list]":
        return self.__dao_usuario.pesquisar(texto)
