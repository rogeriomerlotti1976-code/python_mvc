import flet as ft
# from Utils.BancoUtils import BancoUtils
from View.ViewAutenticacao import ViewAutenticacao
from View.ViewPrincipal import ViewPrincipal


def main(page: ft.Page):
    page.title = 'RMSYS'
    page.window_width = 1100
    page.window_height = 700
    page.window_min_width = 900
    page.window_min_height = 600
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0

    # Em ambiente de desenvolvimento com SQLite, garante que as tabelas
    # utilizadas pelas telas já existam (não afeta MySQL/PostgreSQL).
    # try:
    #     BancoUtils.preparar_sqlite()
    # except Exception as ex:
    #     print(f'Aviso: não foi possível preparar o banco SQLite: {ex}')

    def mostrar_autenticacao():
        page.controls.clear()
        view = ViewAutenticacao(page, on_autenticado=mostrar_principal)
        page.add(view.container)
        page.update()

    def mostrar_principal(usuario_logado: str):
        page.controls.clear()
        view = ViewPrincipal(page, usuario_logado, on_sair=mostrar_autenticacao)
        page.add(view.container)
        page.update()

    mostrar_autenticacao()


if __name__ == '__main__':
    ft.run(main)