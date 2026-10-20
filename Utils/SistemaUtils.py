from pathlib import Path

class SistemaUtils():
    @staticmethod
    def get_diretorio_raiz_sistema() -> str:
        return str(Path(__file__).resolve().parent.parent)

    @staticmethod
    def get_nome_arquivo_config() -> str:
        return SistemaUtils.get_diretorio_raiz_sistema() + r'\config.ini'
