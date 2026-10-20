from Controller.Interface.IControllerUsuario import IControllerUsuario
from Model.Interface.IModelUsuario import IModelUsuario
from Model.Entity.EntityUsuario import EntityUsuario
from Model.Entity.EntityUsuarioInterface import IEntityUsuario

class ControllerUsuario(IControllerUsuario):
    def __init__(self, model_usuario: IModelUsuario):
        self.__model_usuario = model_usuario
        self.__usuario = EntityUsuario()

    @property
    def usuario(self) -> IEntityUsuario:
        return self.__usuario

    #########################################################
    # código gerado pela IA na montagem das telas
    def novo(self) -> None:
        self.__usuario = EntityUsuario()

    def carregar(self, id: int) -> None:
        usuario = self.__model_usuario.consultar_por_id(id)

        if usuario is None:
            raise ValueError('Usuário não encontrado.')

        self.__usuario = usuario
    #########################################################

    def inserir(self) -> int:
        return self.__model_usuario.inserir(self.__usuario)

    def atualizar(self):
        return self.__model_usuario.atualizar(self.__usuario)

    def excluir(self, id: int) :
        return self.__model_usuario.excluir(id)

    def consultar_por_id(self, id: int) -> list:
        return self.__model_usuario.consultar_por_id(id)

    def consultar_por_login(self, login: str) -> IEntityUsuario:
        pass

    def existe(self, login, senha: str) -> bool:
        pass

    def listar_tudo(self) -> "tuple[list, list]":
        return self.__model_usuario.listar_tudo()

    def autenticar(self, login: str, senha: str) -> bool:
        return self.__model_usuario.autenticar(login, senha)

    def pesquisar(self, texto: str) -> "tuple[list, list]":
        return self.__model_usuario.pesquisar(texto)



