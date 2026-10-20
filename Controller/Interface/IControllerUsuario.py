from abc import ABC, abstractmethod
from Model.Entity.EntityUsuarioInterface import IEntityUsuario

class IControllerUsuario(ABC):
    @property
    @abstractmethod
    def usuario(self) -> IEntityUsuario:
        return self.__usuario

    #########################################################
    # código gerado pela IA na montagem das telas
    @abstractmethod
    def novo(self) -> None: pass

    @abstractmethod
    def carregar(self, id: int) -> None: pass
    #########################################################

    @abstractmethod
    def inserir(self) -> int: pass

    @abstractmethod
    def atualizar(self): pass

    @abstractmethod
    def excluir(self, id: int): pass

    @abstractmethod
    def consultar_por_id(self, id: int) -> list: pass

    @abstractmethod
    def consultar_por_login(self, login: str) -> IEntityUsuario: pass

    @abstractmethod
    def existe(self, login, senha: str) -> bool: pass

    @abstractmethod
    def listar_tudo(self) -> "tuple[list, list]": pass

    @abstractmethod
    def autenticar(self, login: str, senha: str) -> bool: pass

    @abstractmethod
    def pesquisar(self, texto: str) -> "tuple[list, list]": pass