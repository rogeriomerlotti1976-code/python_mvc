import flet as ft

class MensagensUtils():
    @staticmethod
    def __fechar_dialog(self, e, dlg):
        self.page.close(dlg)

    @staticmethod
    def exibir_mensagem(self, mensagem: str):
        dlg = ft.AlertDialog(
            title=ft.Text("Aviso"),
            content=ft.Text(mensagem),
            actions=[
                ft.TextButton(
                    "OK",
                    on_click=lambda e: self.fechar_dialog(e, dlg)
                )
            ]
        )

        self.page.open(dlg)


