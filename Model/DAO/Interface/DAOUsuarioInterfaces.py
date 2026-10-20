from abc import ABC, abstractmethod
from Model.Entity.EntityUsuarioInterface import IEntityUsuario
from Model.Entity.EntityUsuario import EntityUsuario

class IUsuarioDAO(ABC):
    @abstractmethod
    def inserir(self, usuario: IEntityUsuario) -> int: pass

    @abstractmethod
    def atualizar(self, usuario: IEntityUsuario): pass

    @abstractmethod
    def excluir(self, id: int) : pass

    @abstractmethod
    def consultar_por_id(self, id: int) -> list: pass

    @abstractmethod
    def consultar_por_login(self, login: str) -> IEntityUsuario: pass

    @abstractmethod
    def existe(self, login: str) -> bool: pass

    @abstractmethod
    def listar_tudo(self) -> "tuple[list, list]": pass

    @abstractmethod
    def autenticar(self, login: str, senha: str) -> bool: pass

    @abstractmethod
    def pesquisar(self, texto: str) -> "tuple[list, list]": pass

