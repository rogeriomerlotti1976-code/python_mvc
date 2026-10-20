from abc import ABC, abstractmethod

class IEntityUsuario(ABC):
    @property
    @abstractmethod
    def id(self) -> int: pass

    @id.setter
    @abstractmethod
    def id(self, value: int) -> None: pass

    @property
    @abstractmethod
    def nome(self) -> str: pass

    @nome.setter
    @abstractmethod
    def nome(self, value: str) -> str: pass

    @property
    @abstractmethod
    def login(self) -> str: pass

    @login.setter
    @abstractmethod
    def login(self, value: str) -> str: pass

    @property
    @abstractmethod
    def senha(self) -> str: pass

    @senha.setter
    @abstractmethod
    def senha(self, value: str) -> str: pass

    @property
    @abstractmethod
    def ativo(self) -> bool: pass

    @ativo.setter
    @abstractmethod
    def ativo(self, value: str) -> bool: pass
