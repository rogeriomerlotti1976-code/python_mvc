from tkinter import messagebox
import flet as ft
from Controller.Factory.ControllerUsuarioFactory import ControllerUsuarioFactory
from Utils import SistemaUtils
# from Controller.Factory.ControllerClienteFactory import ControllerClienteFactory
from View.ViewUsuario import ViewUsuario
from View.ViewCliente import ViewCliente


class ViewPrincipal:
    """Tela principal do sistema.

    Dividida em um painel de menu à esquerda (Usuários, Clientes, ...)
    e uma área de conteúdo à direita, onde é exibida a tela de
    cadastro correspondente à opção selecionada no menu.
    """

    def __init__(self, page: ft.Page, usuario_logado: str, on_sair):
        self.page = page
        self.usuario_logado = usuario_logado
        self.on_sair = on_sair
        self._opcao_selecionada = None

        self.area_conteudo = ft.Container(
            expand=True,
            padding=20,
            content=self._tela_boas_vindas(),
        )

        self.container = ft.Row(
            expand=True,
            spacing=0,
            controls=[
                self._criar_menu(),
                ft.VerticalDivider(width=1),
                self.area_conteudo,
            ],
        )

    def _tela_boas_vindas(self) -> ft.Control:
        return ft.Column(
            controls=[
                ft.Text(f'Bem-vindo(a), {self.usuario_logado}!', size=20, weight=ft.FontWeight.BOLD),
                ft.Text('Selecione uma opção no menu ao lado para começar.'),
            ]
        )

    def _criar_menu(self) -> ft.Control:
        botao_usuarios = ft.ElevatedButton(
            'Usuários', icon=ft.Icons.PEOPLE, width=190,
            on_click=lambda e: self._abrir_tela('usuarios'),
        )
        botao_clientes = ft.ElevatedButton(
            'Clientes', icon=ft.Icons.BADGE, width=190,
            on_click=lambda e: self._abrir_tela('clientes'),
        )
        botao_sair = ft.OutlinedButton(
            'Sair', icon=ft.Icons.LOGOUT, width=190,
            on_click=lambda e: self.on_sair(),
        )

        return ft.Container(
            width=210,
            padding=15,
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Text('Menu', size=18, weight=ft.FontWeight.BOLD),
                    ft.Divider(),
                    botao_usuarios,
                    botao_clientes,
                    ft.Divider(),
                    botao_sair,
                ],
            ),
        )

    # dialogo = ft.AlertDialog(
    #     modal=True,
    #     title=ft.Text('Confirmar exclusão'),
    #     content=ft.Text(
    #         'Deseja realmente excluir o registro selecionado?'
    #     ),
    #     actions=[
    #         ft.TextButton(
    #             'Cancelar',
    #             on_click=cancelar,
    #         ),
    #         ft.TextButton(
    #             'Excluir',
    #             on_click=confirmar,
    #         ),
    #     ],
    #     actions_alignment=ft.MainAxisAlignment.END,
    # )

    # self.page.show_dialog(dialogo)

    def _abrir_tela(self, opcao: str) -> None:
        # Cada acesso ao menu cria a tela (e o controller) novamente,
        # garantindo que a pesquisa exiba os dados mais atuais.
        if opcao == 'usuarios':
            print('ViewPrincipal._abrir_tela')
            controller = ControllerUsuarioFactory().criar()
            tela = ViewUsuario(self.page, controller, on_fechar=self._fechar_tela)
        elif opcao == 'clientes':
            # raise ValueError('Em construção!')
            messagebox.showerror('Aviso', 'Tela em construção')
            return
            # controller = ControllerClienteFactory().criar()
            # tela = ViewCliente(self.page, controller, on_fechar=self._fechar_tela)
        else:
            return

        self._opcao_selecionada = opcao
        self.area_conteudo.content = tela.container
        self.page.update()

    def _fechar_tela(self) -> None:
        self._opcao_selecionada = None
        self.area_conteudo.content = self._tela_boas_vindas()
        self.page.update()
