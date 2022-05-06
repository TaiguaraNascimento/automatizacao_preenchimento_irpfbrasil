import pyautogui as rpa
from principal.execucao.controlador import Controlador

from principal.execucao.declaracao_factory import DeclaracaoFactory
from principal.execucao.gerenciador_de_telas.mapeamento_por_referencia import MapeamentoPorReferencia
from principal.modelos.enums.mapa_da_tela import TamanhosDeTelas
from principal.modelos.enums.sistema import VersaoDoPrograma
from principal.organizador.organizador import Organizador


organizador = Organizador()
print(organizador.__obter_endereco_da_pasta_desktop__())














def testar_controlador():

    mapa = MapeamentoPorReferencia(VersaoDoPrograma.VERSAO_2022, TamanhosDeTelas.TELA_27P_1920_X_1080)
    controlador = Controlador(VersaoDoPrograma.VERSAO_2022)

    controlador.abrir_sistema_da_receita_federal()

    # Obtenção dos dados da declaração de imposto de renda
    arquivo = 'C:\\teste\\arquivo.xlxs'
    declaracao_factory = DeclaracaoFactory(arquivo)
    declaracao = declaracao_factory.obter_declaracao_a_partir_do_arquivo()

    # Executa a preparação de uma nova declaração 
    # controlador.criar_nova_declaracao(declaracao)

    # Cadastrar contribuinte
    # controlador.cadastrar_contribuinte(declaracao)

    # Cadastrar dependentes do declarante
    # controlador.cadastrar_dependentes(declaracao)

    #Cadastrar os ativos da pessoa
    controlador.cadastrar_ativos(declaracao)