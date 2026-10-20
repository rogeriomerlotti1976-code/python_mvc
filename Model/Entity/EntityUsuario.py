from Model.Entity.EntityUsuarioInterface import IEntityUsuario

class EntityUsuario(IEntityUsuario):
    def __init__(self):
        self.__id = 0
        self.__nome = ''
        self.__login = ''
        self.__senha = ''
        self.__ativo = 1

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int) -> None:
        if value < 0:
            raise ValueError("O ID não pode ser negativo.")

        self.__id = value

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, value: str) -> str:
        if value.strip() == '':
            raise ValueError("O nome do usuário deve ser preenchido.")

        self.__nome = value

    @property
    def login(self) -> str:
        return self.__login

    @login.setter
    def login(self, value: str) -> str:
        if value.strip() == '':
            raise ValueError("O login do usuário deve ser preenchido.")

        self.__login = value

    @property
    def senha(self) -> str:
        return self.__senha

    @senha.setter
    def senha(self, value: str) -> str:
        if value.strip() == '':
            raise ValueError("A senha do usuário deve ser preenchido.")

        self.__senha = value

    @property
    def ativo(self) -> bool:
        return self.__ativo

    @ativo.setter
    def ativo(self, value: str) -> bool:
        self.__ativo = value