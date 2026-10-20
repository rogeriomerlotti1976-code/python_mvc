import flet as ft
from Controller.Factory.ControllerUsuarioFactory import ControllerUsuarioFactory


class ViewAutenticacao:
    """Tela de autenticação (login) do sistema."""

    def __init__(self, page: ft.Page, on_autenticado):
        self.page = page
        self.on_autenticado = on_autenticado
        self.controller_usuario = ControllerUsuarioFactory().criar()

        self.campo_login = ft.TextField(
            label='Usuário', width=280, autofocus=True, on_submit=self._entrar_clicked
        )
        self.campo_senha = ft.TextField(
            label='Senha', width=280, password=True, can_reveal_password=True,
            on_submit=self._entrar_clicked,
        )
        self.texto_mensagem = ft.Text(value='', color=ft.Colors.RED)

        self.container = ft.Container(
            alignment=ft.alignment.Alignment.CENTER,
            expand=True,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,
                controls=[
                    ft.Text('RMSYS', size=32, weight=ft.FontWeight.BOLD),
                    ft.Text('Acesso ao sistema', size=16, color=ft.Colors.GREY_700),
                    self.campo_login,
                    self.campo_senha,
                    ft.ElevatedButton(
                        'Entrar', icon=ft.Icons.LOGIN, width=280, on_click=self._entrar_clicked
                    ),
                    self.texto_mensagem,
                ],
            ),
        )

    def _entrar_clicked(self, e):
        login = (self.campo_login.value or '').strip()
        senha = (self.campo_senha.value or '').strip()

        if not login or not senha:
            self._mostrar_mensagem('Informe usuário e senha.')
            return

        try:
            if self.controller_usuario.autenticar(login, senha):
                self._mostrar_mensagem('')
                self.on_autenticado(login)
            else:
                self._mostrar_mensagem('Usuário ou senha inválidos.')
        except Exception as ex:
            self._mostrar_mensagem(f'Não foi possível autenticar: {ex}')

    def _mostrar_mensagem(self, texto: str):
        self.texto_mensagem.value = texto
        self.page.update()
