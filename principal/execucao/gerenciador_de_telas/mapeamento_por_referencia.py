from typing import List
from principal.execucao.gerenciador_de_telas.mapeamento import Mapeamento
from principal.execucao.posicoes import Posicoes
from principal.modelos.enums.contribuinte import DeclaracaoRetificada, TiposDeDeclaracao
from principal.modelos.enums.mapa_da_tela import NovaDeclaracao, PosicoesSecaoBensEDireitos, PosicoesSecaoDependentes, SecoesDoSistema, TamanhosDeTelas
from principal.modelos.enums.sistema import VersaoDoPrograma


class MapeamentoPorReferencia(Mapeamento):
    
    def __init__(self, versao_do_programa: VersaoDoPrograma, tamanho_da_tela: TamanhosDeTelas) -> None:
        self.versao_do_programa = versao_do_programa
        self.tamanho_da_tela = tamanho_da_tela
    

    def secoes_do_menu_lateral(self, sessao_do_sistema: SecoesDoSistema, tipo_de_declaracao: TiposDeDeclaracao) -> Posicoes:

        if self.tamanho_da_tela == TamanhosDeTelas.TELA_27P_1920_X_1080:  
            matriz_de_posicoes = self.obter_tabela_do_menu_lateral_27P()      

        linha = sessao_do_sistema.value - 1     # Usa a ordem do Enum para identifica-lo no array
        coluna = tipo_de_declaracao.value       # Considera o tipo de declaração como a posição das colunas do array

        posicao_de_retorno = matriz_de_posicoes[linha][coluna]
        
        return Posicoes(posicao_de_retorno[0], posicao_de_retorno[1])



    def posicao_na_tela_de_cadastro_de_contribuinte(self, tipo_de_declaracao: DeclaracaoRetificada, tamanho_da_tela: TamanhosDeTelas) -> Posicoes:

        if tamanho_da_tela == TamanhosDeTelas.TELA_27P_1920_X_1080:
            matriz_de_posicoes = self.obter_tabela_da_secao_de_identificao_do_contribuinte()


        linha = tipo_de_declaracao.value - 1    # Usa a ordem do Enum para identifica-lo no array
        coluna = tamanho_da_tela.value       # Considera o tamanho da tela como a posição das colunas do array

        posicao_de_retorno = matriz_de_posicoes[linha][coluna]
        
        return Posicoes(posicao_de_retorno[0], posicao_de_retorno[1])



    def posicao_na_tela_cadastro_de_dependentes(self, tamanho_da_tela: TamanhosDeTelas, posicoes_secao_dependentes: PosicoesSecaoDependentes):

        if tamanho_da_tela == TamanhosDeTelas.TELA_27P_1920_X_1080:
            matriz_de_posicoes = self.obter_tabela_da_secao_de_dependentes()


        linha = posicoes_secao_dependentes.value - 1    # Usa a ordem do Enum para identifica-lo no array
        coluna = tamanho_da_tela.value       # Considera o tamanho da tela como a posição das colunas do array

        posicao_de_retorno = matriz_de_posicoes[linha][coluna]
        
        return Posicoes(posicao_de_retorno[0], posicao_de_retorno[1])


    def posicao_na_tela_cadastro_de_bens_e_direitos(self, tamanho_da_tela: TamanhosDeTelas, posicoes_secao_bens_e_direitos: PosicoesSecaoBensEDireitos):

        if tamanho_da_tela == TamanhosDeTelas.TELA_27P_1920_X_1080:
            matriz_de_posicoes = self.obter_tabela_da_secao_de_bens_e_direitos()


        linha = posicoes_secao_bens_e_direitos.value - 1    # Usa a ordem do Enum para identifica-lo no array
        coluna = tamanho_da_tela.value       # Considera o tamanho da tela como a posição das colunas do array

        posicao_de_retorno = matriz_de_posicoes[linha][coluna]
        
        return Posicoes(posicao_de_retorno[0], posicao_de_retorno[1])


    def obter_tabela_da_secao_de_bens_e_direitos(self) -> List:
        matriz_de_posicoes = []
        matriz_de_posicoes.append([PosicoesSecaoBensEDireitos.BOTAO_NOVO,             (1668,987),      (0,0)])
        matriz_de_posicoes.append([PosicoesSecaoBensEDireitos.BOTAO_OK_CADASTRAR,     (1651,1031),      (0,0)])
        return matriz_de_posicoes



    def abertura_de_nova_declaracao(self, item_de_tela: NovaDeclaracao):
        try:
            if self.tamanho_da_tela == TamanhosDeTelas.TELA_27P_1920_X_1080:
                match item_de_tela:
                    case NovaDeclaracao.BOTAO_NOVA_DECLARACAO:                                return Posicoes(41, 219)
                    case NovaDeclaracao.OPCAO_DECLARACAO_DE_AJUSTE_ANUAL:                     return Posicoes(794,566)
                    case NovaDeclaracao.OPCAO_DECLARACAO_FINAL_DE_ESPOLIO:                    return Posicoes(790,595)
                    case NovaDeclaracao.OPCAO_DECLARACAO_DE_SAIDA_DEFINITIVA:                 return Posicoes(790,622)
                    case NovaDeclaracao.BOTAO_INICIAR_DECLARACAO_EM_BRANCO:                   return Posicoes(1135,644)
                    case NovaDeclaracao.CAIXA_INSERCAO_DO_CPF:                                return Posicoes(788, 729)
                    case NovaDeclaracao.CAIXA_INSERCAO_DO_NOME:                               return Posicoes(1003, 732)
                    case NovaDeclaracao.BOTAO_OK_DECLARACAO_EM_BRANCO:                        return Posicoes(1410, 728)
                    case NovaDeclaracao.BOTAO_OK_CONFIRMACAO:                                 return Posicoes(908, 625)

            elif self.tamanho_da_tela == TamanhosDeTelas.TELA_156P_1366_768:
                match item_de_tela:
                    case NovaDeclaracao.BOTAO_NOVA_DECLARACAO:                                return Posicoes(61, 209)
                    case NovaDeclaracao.OPCAO_DECLARACAO_DE_AJUSTE_ANUAL:                     return Posicoes(779,566)
                    case NovaDeclaracao.OPCAO_DECLARACAO_FINAL_DE_ESPOLIO:                    return Posicoes(784,590)
                    case NovaDeclaracao.OPCAO_DECLARACAO_DE_SAIDA_DEFINITIVA:                 return Posicoes(780,622)
                    case NovaDeclaracao.BOTAO_INICIAR_DECLARACAO_EM_BRANCO:                   return Posicoes(871, 496)
                    case NovaDeclaracao.CAIXA_INSERCAO_DO_CPF:                                return Posicoes(576, 611)
                    case NovaDeclaracao.CAIXA_INSERCAO_DO_NOME:                               return Posicoes(751, 605)
                    case NovaDeclaracao.BOTAO_OK_DECLARACAO_EM_BRANCO:                        return Posicoes(1123, 603)
                    case NovaDeclaracao.BOTAO_OK_CONFIRMACAO:                                 return Posicoes(639, 468)
        except:
            print('Não foi possível selecionar nenhum item na abertura do sistema.')


    def obter_tabela_da_secao_de_identificao_do_contribuinte(self) -> List:
        """Método que devolve uma matriz que correlaciona tamanho de tela com o tipo de declaração."""
        
        matriz_de_posicoes = []
        matriz_de_posicoes.append([DeclaracaoRetificada.SIM,        (803,269),         (0,0)])
        matriz_de_posicoes.append([DeclaracaoRetificada.NAO,        (472,267),         (0,0)])
        return matriz_de_posicoes


    def obter_tabela_do_menu_lateral_27P(self) -> List:

        """Método que devolve uma matriz que correlaciona tipo de declaração e a seção desejada para esse tamanho de tela. """

        px = 60 # Posição X, que em tese não varia porque estão todos alinhados
        matriz_de_posicoes = []
        matriz_de_posicoes.append([SecoesDoSistema.SECAO_IDENTIFICACAO_DO_CONTRIBUINTE,                                    (px, 197),       (px, 201),      (px, 195)])
        matriz_de_posicoes.append([SecoesDoSistema.SECAO_SAIDA_DEFINITIVA,                                                 (px, 000),       (px, 000),      (px, 221)])
        matriz_de_posicoes.append([SecoesDoSistema.SECAO_ESPOLIO,                                                          (px, 666),       (px, 228),      (px, 000)])
        matriz_de_posicoes.append([SecoesDoSistema.SECAO_DEPENDENTES,                                                      (px, 218),       (px, 247),      (px, 252)])
        matriz_de_posicoes.append([SecoesDoSistema.SECAO_ALIMENTANDOS,                                                     (px, 244),       (px, 282),      (px, 279)])
        matriz_de_posicoes.append([SecoesDoSistema.SECAO_HERDEIROS_MEIEIROS,                                               (px, 000),       (px, 312),      (px, 312)])
        matriz_de_posicoes.append([SecoesDoSistema.SECAO_RENDIMENTOS_TRIBUTAVEIS_RECEBIDOS_DE_PJ,                          (px, 277),       (px, 347),      (px, 346)])
        matriz_de_posicoes.append([SecoesDoSistema.SECAO_RENDIMENTOS_RECEBIDOS_DE_PF_OU_EXTERIOR,                          (px, 311),       (px, 367),      (px, 363)])
        matriz_de_posicoes.append([SecoesDoSistema.SECAO_RENDIMENTOS_ISENTOS_E_NAO_TRIBUTAVEIS,                            (px, 338),       (px, 391),      (px, 390)])
        matriz_de_posicoes.append([SecoesDoSistema.SECAO_RENDIMENTOS_SUJEITOS_A_TRIBUTACAO_EXCLUSIVA_DEFINITIVA,           (px, 370),       (px, 426),      (px, 448)])
        matriz_de_posicoes.append([SecoesDoSistema.SECAO_RENDIMENTOS_TRIBUTAVEIS_DE_PJ_SUSPENSA,                           (px, 406),       (px, 470),      (px, 10)])
        matriz_de_posicoes.append([SecoesDoSistema.SECAO_RENDIMENTOS_RECEBIDOS_ACUMULATIVAMENTE,                           (px, 451),       (px, 519),      (px, 477)])
        matriz_de_posicoes.append([SecoesDoSistema.SECAO_IMPOSTO_RETIDO_PAGO,                                              (px, 482),       (px, 539),      (px, 505)])
        matriz_de_posicoes.append([SecoesDoSistema.SECAO_PAGAMENTOS_EFETUADOS,                                             (px, 512),       (px, 562),      (px, 538)])
        matriz_de_posicoes.append([SecoesDoSistema.SECAO_DOACOES_EFETUADAS,                                                (px, 540),       (px, 597),      (px, 562)])
        matriz_de_posicoes.append([SecoesDoSistema.SECAO_DOACOES_DIRETAMENTE_NA_DECLARACAO,                                (px, 564),       (px, 620),      (px, 596)])
        matriz_de_posicoes.append([SecoesDoSistema.SECAO_BENS_E_DIREITOS,                                                  (px, 599),       (px, 657),      (px, 632)])
        matriz_de_posicoes.append([SecoesDoSistema.SECAO_DIVIDAS_E_ONUS_REAIS,                                             (px, 627),       (px, 682),      (px, 650)])
        matriz_de_posicoes.append([SecoesDoSistema.SECAO_DOACOES_A_PARTIDOS_POLITICOS_E_CANDIDATOS,                        (px, 686),       (px, 721),      (px, 683)])

        return matriz_de_posicoes


    def obter_tabela_da_secao_de_dependentes(self) -> List:
        matriz_de_posicoes = []
        matriz_de_posicoes.append([PosicoesSecaoDependentes.BOTAO_NOVO,             (1654,986),      (0,0)])
        matriz_de_posicoes.append([PosicoesSecaoDependentes.BOTAO_OK_CADASTRAR,     (1650,1027),      (0,0)])
        return matriz_de_posicoes






















