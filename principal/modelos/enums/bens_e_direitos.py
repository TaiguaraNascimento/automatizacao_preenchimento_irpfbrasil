from enum import Enum

class TiposDeAtivos(Enum):
    BENS_IMOVEIS = '01'
    BENS_MOVEIS = '02'
    PARTICIPACOES_SOCIETARIAS = '03'
    APLICAVOES_E_INVESTIMENTOS = '04'
    CREDITOS = '05'
    DEPOSITOS_A_VISTA = '06'
    FUNDOS = '07'
    CRIPTOATIVOS = '08'
    OUTROS = '99'


class TiposDeImoveis(Enum):
    PREDIO_RESIDENCIAL = '01'
    PREDIO_COMERCIAL = '02'
    GALPAO = '03'
    APARTAMENTO = '11'
    CASA = '12'
    TERRENO = '13'
    IMOVEL_RURAL = '14'
    SALA_OU_CONJUNTO = '15'
    CONSTRUCAO = '16'
    BENFEITORIAS = '17'
    LOJA = '18'
    OUTROS_BENS = '99'


class UnidadeDeMedida(Enum):
    M2 = 1
    HA = 2
    

class RegistroEmCartorio(Enum):
    SIM = 1
    NAO = 2


class TiposdDeBensMoveis(Enum):
    VEICULO_AUTOMOTOR = '01'
    AERONAVE = '02'
    EMBARCACAO = '03'
    BENS_DE_ATIVIDADE_AUTONOMA = '04'
    JOIAS_ARTES_ETC = '05'
    OUTROS_BENS_MOVEIS = '99'


class TiposDeAplicacoesInvestimentos(Enum):
    DEPOSITOS_EM_CONTA_POUPANCA = '01'
    TITULOS_ISENTOS_DE_TRIBUTACAO = '02'
    TITULOS_SUJEITOS_A_TRIBUTACAO = '03'
    ATIVOS_NEGOCIADOS_EM_BOLSA = '04'
    OURO_ATIVO_FINANCEIRO = '05'
    OUTRAS_APLICACOES_E_FINANCIAMENTOS = '99'


class TiposDeDepositosAVista(Enum):
    DEPOSITOS_EM_CONTA_CORRENTE = '01'
    DINHEIRO_NACIONAL_EM_ESPECIE = '10'
    DINHEIRO_ESTRANGEIRO_EM_ESPECIE = '11'
    OUTROS_DEPOSITOS = '99'


class ProprietarioDeUmAtivo(Enum):
    TITULAR = 1
    DEPENDENTE = 1


class TiposDeParticipacoesSocietarias(Enum):
    ACOES = '01'
    QUOTAS_OU_QUINHOES_DE_CAPITAL = '02'
    OUTRAS_PARTICIPACOES = '99'
