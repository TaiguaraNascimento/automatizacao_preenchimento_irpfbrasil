from enum import Enum

class TipoDeProcessamento(Enum):
    POR_IMAGEM = 1
    POR_POSICAO_FIXA_NA_TELA = 2


class VersaoDoPrograma(Enum):
    VERSAO_2022 = 1