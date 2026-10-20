import flet as ft
from View.Componentes.ViewCadastroBase import ViewCadastroBase


class ViewCliente(ViewCadastroBase):
    """Tela de cadastro de Clientes (pesquisa + inserir/alterar/excluir)."""

    def __init__(self, page: ft.Page, controller, on_fechar=None):
        self.campo_nome = ft.TextField(label='Nome', width=350)
        self.campo_email = ft.TextField(label='E-mail', width=300)
        self.campo_telefone = ft.TextField(label='Telefone', width=200)
        super().__init__(page, controller, 'Clientes', on_fechar)

    def criar_colunas_grid(self) -> list:
        return [
            ft.DataColumn(ft.Text('Código')),
            ft.DataColumn(ft.Text('Nome')),
            ft.DataColumn(ft.Text('E-mail')),
            ft.DataColumn(ft.Text('Telefone')),
        ]

    def criar_campos_formulario(self) -> list:
        return [
            ft.Row(controls=[self.campo_nome]),
            ft.Row(controls=[self.campo_email, self.campo_telefone]),
        ]

    def preencher_formulario(self, cliente) -> None:
        self.campo_nome.value = cliente.nome
        self.campo_email.value = cliente.email
        self.campo_telefone.value = cliente.telefone

    def ler_formulario(self, cliente) -> None:
        cliente.nome = (self.campo_nome.value or '').strip()
        cliente.email = (self.campo_email.value or '').strip()
        cliente.telefone = (self.campo_telefone.value or '').strip()

    @property
    def entidade_atual(self):
        return self.controller.cliente
