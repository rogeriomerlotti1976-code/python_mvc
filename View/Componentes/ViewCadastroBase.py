import flet as ft


class ViewCadastroBase:
    """Componente base reutilizável para as telas de cadastro (CRUD).

    Implementa o comportamento comum a qualquer tela de cadastro do
    sistema:

    - Modo de PESQUISA: campo de busca + grid (DataTable) + botões
      Inserir, Alterar, Excluir e Fechar.
    - Modo de EDIÇÃO: formulário + botões Gravar e Voltar (retorna ao
      modo de pesquisa sem gravar).

    As telas concretas (ex.: ViewUsuario, ViewCliente) apenas precisam
    descrever as colunas do grid, os campos do formulário e como
    transferir dados entre o formulário e a entidade do controller.
    """

    def __init__(self, page: ft.Page, controller, titulo: str, on_fechar=None):
        self.page = page
        self.controller = controller
        self.titulo = titulo
        self.on_fechar = on_fechar

        self._id_selecionado = None
        self._novo_registro = True

        self.campo_pesquisa = ft.TextField(
            label='Pesquisar', expand=True, on_submit=self._pesquisar_clicked
        )
        self.tabela = ft.DataTable(columns=self.criar_colunas_grid(), rows=[])
        self.texto_mensagem = ft.Text(value='', color=ft.Colors.RED)

        self.container = ft.Column(expand=True, spacing=10)
        self._exibir_pesquisa()

    # ------------------------------------------------------------------
    # Métodos que as telas concretas devem implementar
    # ------------------------------------------------------------------
    def criar_colunas_grid(self) -> list:
        raise NotImplementedError

    def criar_campos_formulario(self) -> list:
        raise NotImplementedError

    def preencher_formulario(self, entidade) -> None:
        raise NotImplementedError

    def ler_formulario(self, entidade) -> None:
        raise NotImplementedError

    @property
    def entidade_atual(self):
        raise NotImplementedError

    def criar_linha_grid(self, registro) -> ft.DataRow:
        """Implementação padrão: assume que a primeira coluna do
        registro é o identificador (ID) e monta uma célula de texto
        para cada coluna retornada pela pesquisa/listagem."""
        linha = ft.DataRow(
            cells=[ft.DataCell(ft.Text('' if valor is None else str(valor))) for valor in registro]
        )
        id_registro = registro[0]

        def selecionar(e, id_registro=id_registro, linha=linha):
            self._selecionar_linha(id_registro, linha)

        linha.on_select_change = selecionar
        return linha


    # ------------------------------------------------------------------
    # Modo pesquisa
    # ------------------------------------------------------------------
    def _exibir_pesquisa(self):
        self._atualizar_grid()

        barra_pesquisa = ft.Row(
            controls=[
                self.campo_pesquisa,
                ft.ElevatedButton('Pesquisar', icon=ft.Icons.SEARCH, on_click=self._pesquisar_clicked),
            ]
        )

        barra_botoes = ft.Row(
            controls=[
                ft.ElevatedButton('Inserir', icon=ft.Icons.ADD, on_click=self._inserir_clicked),
                ft.ElevatedButton('Alterar', icon=ft.Icons.EDIT, on_click=self._alterar_clicked),
                ft.ElevatedButton(
                    'Excluir', icon=ft.Icons.DELETE,
                    color=ft.Colors.WHITE, bgcolor=ft.Colors.RED_400,
                    on_click=self._excluir_clicked,
                ),
                ft.OutlinedButton('Fechar', icon=ft.Icons.CLOSE, on_click=self._fechar_clicked),
            ]
        )

        self.container.controls = [
            ft.Text(self.titulo, size=22, weight=ft.FontWeight.BOLD),
            barra_pesquisa,
            ft.Container(content=ft.Column([self.tabela], scroll=ft.ScrollMode.AUTO), expand=True),
            barra_botoes,
            self.texto_mensagem,
        ]
        self._atualizar_pagina()

    def _atualizar_grid(self, registros=None):
        try:
            if registros is None:
                _, registros = self.controller.listar_tudo()
            self.tabela.rows = [self.criar_linha_grid(registro) for registro in registros]
        except Exception as ex:
            self.tabela.rows = []
            self._mostrar_mensagem(f'Erro ao carregar dados: {ex}')

        self._id_selecionado = None

    def _pesquisar_clicked(self, e):
        texto = (self.campo_pesquisa.value or '').strip()
        try:
            if texto:
                _, registros = self.controller.pesquisar(texto)
            else:
                _, registros = self.controller.listar_tudo()
            self._atualizar_grid(registros)
            self._mostrar_mensagem('')
        except Exception as ex:
            self._mostrar_mensagem(f'Erro na pesquisa: {ex}')
        self._atualizar_pagina()

    def _selecionar_linha(self, id_registro, linha_selecionada: ft.DataRow):
        for linha in self.tabela.rows:
            linha.selected = linha is linha_selecionada
        self._id_selecionado = id_registro
        self._atualizar_pagina()

    # ------------------------------------------------------------------
    # Modo edição
    # ------------------------------------------------------------------
    def _inserir_clicked(self, e):
        self.controller.novo()
        self._novo_registro = True
        self._exibir_formulario()

    def _alterar_clicked(self, e):
        if self._id_selecionado is None:
            self._mostrar_mensagem('Selecione um registro na lista para alterar.')
            self._atualizar_pagina()
            return

        try:
            self.controller.carregar(self._id_selecionado)
            self._novo_registro = False
            self._exibir_formulario()
        except Exception as ex:
            self._mostrar_mensagem(f'Erro ao carregar registro: {ex}')
            self._atualizar_pagina()

    def _excluir_clicked(self, e):
        if self._id_selecionado is None:
            self._mostrar_mensagem(
                'Selecione um registro na lista para excluir.'
            )
            self._atualizar_pagina()
            return

        # Guarda o ID antes de abrir o diálogo.
        id_selecionado = self._id_selecionado

        def confirmar(e):
            try:
                self.controller.excluir(id_selecionado)
                self.page.pop_dialog()
                self._exibir_pesquisa()
                self._mostrar_mensagem('Registro excluído com sucesso.')
            except Exception as ex:
                self.page.pop_dialog()
                self._mostrar_mensagem(f'Erro ao excluir: {ex}')
                self._atualizar_pagina()

        def cancelar(e):
            self.page.pop_dialog()

        dialogo = ft.AlertDialog(
            modal=True,
            title=ft.Text('Confirmar exclusão'),
            content=ft.Text(
                'Deseja realmente excluir o registro selecionado?'
            ),
            actions=[
                ft.TextButton(
                    'Cancelar',
                    on_click=cancelar,
                ),
                ft.TextButton(
                    'Excluir',
                    on_click=confirmar,
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        self.page.show_dialog(dialogo)

    def _exibir_formulario(self):
        self.preencher_formulario(self.entidade_atual)
        barra_botoes = ft.Row(
            controls=[
                ft.ElevatedButton('Gravar', icon=ft.Icons.SAVE, on_click=self._gravar_clicked),
                ft.OutlinedButton('Voltar', icon=ft.Icons.ARROW_BACK, on_click=self._voltar_clicked),
            ]
        )

        subtitulo = 'Novo registro' if self._novo_registro else 'Alteração de registro'

        self.container.controls = [
            ft.Text(f'{self.titulo} - {subtitulo}', size=22, weight=ft.FontWeight.BOLD),
            *self.criar_campos_formulario(),
            barra_botoes,
            self.texto_mensagem,
        ]
        self._mostrar_mensagem('')
        self._atualizar_pagina()

    def _gravar_clicked(self, e):
        try:
            self.ler_formulario(self.entidade_atual)

            if self._novo_registro:
                self.controller.inserir()
            else:
                self.controller.atualizar()

            self._exibir_pesquisa()
            self._mostrar_mensagem('Registro gravado com sucesso.')
        except Exception as ex:
            self._mostrar_mensagem(f'Erro ao gravar: {ex}')
        self._atualizar_pagina()

    def _voltar_clicked(self, e):
        self._exibir_pesquisa()

    def _fechar_clicked(self, e):
        if self.on_fechar:
            self.on_fechar()

    # ------------------------------------------------------------------
    # Utilitários
    # ------------------------------------------------------------------
    def _mostrar_mensagem(self, texto: str):
        self.texto_mensagem.value = texto

    def _atualizar_pagina(self):
        if self.page:
            self.page.update()