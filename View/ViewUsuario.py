import flet as ft
from View.Componentes.ViewCadastroBase import ViewCadastroBase


class ViewUsuario(ViewCadastroBase):
    """Tela de cadastro de Usuários (pesquisa + inserir/alterar/excluir)."""

    def __init__(self, page: ft.Page, controller, on_fechar=None):
        self.campo_nome = ft.TextField(label='Nome', width=350)
        self.campo_login = ft.TextField(label='Login', width=250)
        self.campo_senha = ft.TextField(
            label='Senha', width=250, password=True, can_reveal_password=True
        )
        super().__init__(page, controller, 'Usuários', on_fechar)

    def criar_colunas_grid(self) -> list:
        return [
            ft.DataColumn(ft.Text('Código')),
            ft.DataColumn(ft.Text('Nome')),
            ft.DataColumn(ft.Text('Login')),
        ]

    def criar_campos_formulario(self) -> list:
        return [
            ft.Row(controls=[self.campo_nome]),
            ft.Row(controls=[self.campo_login, self.campo_senha]),
        ]

    def preencher_formulario(self, entidade) -> None:
        try:
            self.campo_nome.value = entidade.nome
            self.campo_login.value = entidade.login
            self.campo_senha.value = entidade.senha
        except Exception as e:
            raise ValueError(f'Erro no preencher_formulario: {e}')

    def ler_formulario(self, entidade) -> None:
        entidade.nome = (self.campo_nome.value or '').strip()
        entidade.login = (self.campo_login.value or '').strip()
        entidade.senha = (self.campo_senha.value or '').strip()

    @property
    def entidade_atual(self):
        return self.controller.usuario
