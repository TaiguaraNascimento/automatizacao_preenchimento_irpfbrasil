from enum import Enum

class AlteracoesCadastrais(Enum):
    SIM = 1
    NAO = 0


class TipoDeDependente(Enum):
    COMPANHEIRO = 11
    FILHO_ENTEADO_ATE_21_ANOS = 21
    FILHO_ENTEADO_CURSANDO_SUPERIOR_ATE_24_ANOS = 22
    FILHO_ENTEADO_COM_DEFICIENCIA = 23
    IRMAO_NETO_BISNETO_ATE_21_ANOS = 24
    IRMAO_NETO_BISNETO_CURSANDO_SUPERIOR_ATE_24_ANOS = 25
    IRMAO_NETO_BISNETO_COM_DEFICIENCIA = 26
    PAIS_AVOS_BISAVOS = 31
    MENOR_POBRE = 41
    PESSOA_INCAPAZ = 51


class SaidaDoPais(Enum):
    SIM = 1
    NAO = 2

class PossuiConjuge(Enum):
    SIM = 1
    NAO = 2



class PessoaComDeficiencia(Enum):
    SIM = 1
    NAO = 2


class VersaoDaDeclaracao(Enum):
    ORIGINAL = 1
    RETIFICADORA = 2



class TiposDeDeclaracao(Enum):
    AJUSTE_ANUAL = 1
    FINAL_ESPOLIO = 2
    SAIDA_DEFINITIVA = 3


class DeclaracaoRetificada(Enum):
    SIM = 1
    NAO = 2

class LocalizacaoDoEndereco(Enum):
    BRASIL = 1
    EXTERIOR = 2