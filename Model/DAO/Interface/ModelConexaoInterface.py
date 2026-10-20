from abc import ABC, abstractmethod

class IModelConexao(ABC):
    @abstractmethod
    def conectar(self): pass