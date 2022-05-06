from telnetlib import theNULL
import pyautogui as rpa
from time import sleep
from principal.execucao.gerenciador_de_telas.mapeamento_por_referencia import MapeamentoPorReferencia
from principal.execucao.posicoes import Posicoes
from principal.modelos.ativos.ativos import Ativos
from principal.modelos.ativos.bens_imoveis import Imoveis
from principal.modelos.ativos.bens_investimentos import AplicacoesInvestimentos
from principal.modelos.ativos.bens_moveis import BensMoveis
from principal.modelos.ativos.participacoes_societarias import ParticipacoesSocietarias
from principal.modelos.cadastros.declaracao import Declaracao
from principal.modelos.enums.bens_e_direitos import ProprietarioDeUmAtivo, RegistroEmCartorio, TiposDeAplicacoesInvestimentos, TiposDeAtivos, TiposDeImoveis, TiposdDeBensMoveis, UnidadeDeMedida
from principal.modelos.enums.contribuinte import AlteracoesCadastrais, DeclaracaoRetificada, LocalizacaoDoEndereco, PessoaComDeficiencia, PossuiConjuge, SaidaDoPais, TiposDeDeclaracao
from principal.modelos.enums.mapa_da_tela import NovaDeclaracao, PosicoesSecaoBensEDireitos, PosicoesSecaoDependentes, SecoesDoSistema, TamanhosDeTelas
import pyperclip as memoria

from principal.modelos.enums.sistema import VersaoDoPrograma


class Controlador:

    def __init__(self, versao_do_programa: VersaoDoPrograma) -> None:
        self.tamanho_da_tela = self.descobrir_o_tamanho_da_tela()
        self.versao_do_programa = versao_do_programa
        self.mapa_do_sistema = MapeamentoPorReferencia(self.versao_do_programa, self.tamanho_da_tela)
        self.tempo_de_espera_padrao = 1


    def descrever_acao(funcao):
        """Decorator que demonstra o nome da função que foi executada no terminal."""
        def wrapper(*args, **kargs):
            funcao(*args, **kargs)
            print('> Executou: ', funcao.__name__)
        return wrapper
        

    def descobrir_o_tamanho_da_tela(self) -> TamanhosDeTelas:
        if rpa.size().width == 1366 and rpa.size().height == 768:
            return TamanhosDeTelas.TELA_156P_1366_768
        elif rpa.size().width == 1920 and rpa.size().height == 1080:
            return TamanhosDeTelas.TELA_27P_1920_X_1080
        else:
            print("Nenhum tamanho de tela foi identificado para esse notebook.")


    def alterar_tempo_de_espera_padrao(self, tempo_de_espera) -> None:
        """Método que altera o tempo padrão adotado pela classe para os processamentos internos."""
        self.tempo_de_espera_padrao = tempo_de_espera


    def esperar_mais_tempo(self) -> None:
        """Método que faz o sistema esperar 10x o tempo padrão para carregar o arquivo."""
        sleep(self.tempo_de_espera_padrao * 10)


    def esperar(self) -> None:
        sleep(self.tempo_de_espera_padrao)

    
    def pular_campo(self) -> None:
        rpa.press('tab')
    

    def pressionar_espaco(self) -> None:
        rpa.press('space')


    def pressionar_enter(self) -> None:
        rpa.press('enter')


    def escrever_no_campo(self, conteudo: str) -> None:
        rpa.write(conteudo.upper())


    def setas_a_direita(self) -> None:
        rpa.press('right')

    def setas_para_baixo(self) -> None:
        rpa.press('down')

    def clicar_na_posicao(self, posicao: Posicoes):
        """Este método abstrai todo o esforço para se realizar o mapeamento e os cliques em tela."""
        try:
            rpa.click(posicao.posicao_x, posicao.posicao_y)
            self.esperar()
        except:
            print('Não foi possível realizar a ação de clicar automaticamente.')

    
    @descrever_acao
    def focar_na_janela_correta(self):
        try:
            rpa.getWindowsWithTitle(self.mapa_do_sistema.titulo_do_sistema_por_versao(self.versao_do_programa))[0].maximize()
        except:
            pass


    @descrever_acao
    def abrir_sistema_da_receita_federal(self) -> None:
        rpa.hotkey('winleft', 'd')
        try:
            self.focar_na_janela_correta()
        except:
            try:
                rpa.hotkey('winleft', 's')
                rpa.write(self.mapa_do_sistema.nome_da_instalacao_por_versao(self.versao_do_programa))
                self.pressionar_enter()
                self.esperar_mais_tempo()
            except:
                print('Não foi possível abrir o programa do IRPF.')

    
    @descrever_acao
    def criar_nova_declaracao(self, declaracao: Declaracao) -> None:

        # Apontar para a janela
        self.focar_na_janela_correta()

        # Criar uma nova declaração
        posicao_do_clique = self.mapa_do_sistema.abertura_de_nova_declaracao(NovaDeclaracao.BOTAO_NOVA_DECLARACAO)
        self.clicar_na_posicao(posicao_do_clique)

        # Escolhe o tipo de declaração
        if declaracao.tipo_de_declaracao == TiposDeDeclaracao.AJUSTE_ANUAL:
            posicao_do_clique = self.mapa_do_sistema.abertura_de_nova_declaracao(NovaDeclaracao.OPCAO_DECLARACAO_DE_AJUSTE_ANUAL)
            self.clicar_na_posicao(posicao_do_clique)

        elif declaracao.tipo_de_declaracao == TiposDeDeclaracao.FINAL_ESPOLIO:
            posicao_do_clique = self.mapa_do_sistema.abertura_de_nova_declaracao(NovaDeclaracao.OPCAO_DECLARACAO_FINAL_DE_ESPOLIO)
            self.clicar_na_posicao(posicao_do_clique)
  
        elif declaracao.tipo_de_declaracao == TiposDeDeclaracao.SAIDA_DEFINITIVA:
            posicao_do_clique = self.mapa_do_sistema.abertura_de_nova_declaracao(NovaDeclaracao.OPCAO_DECLARACAO_DE_SAIDA_DEFINITIVA)
            self.clicar_na_posicao(posicao_do_clique)


        # Iniciar uma nova declaração em branco
        posicao_do_clique = self.mapa_do_sistema.abertura_de_nova_declaracao(NovaDeclaracao.BOTAO_INICIAR_DECLARACAO_EM_BRANCO)
        self.clicar_na_posicao(posicao_do_clique)
        
        # Registrar o CPF
        # Não é necessário apontar para NovaDeclaracao.CAIXA_INSERCAO_DO_CPF: o sistema já libera o foco
        self.escrever_no_campo(declaracao.contribuinte.cpf)
        self.pular_campo() # Nesserário porque o sistema do IRPF tem problema em alguns componentes e direciona para o nome direto

        # Registrar o nome
        self.escrever_no_campo(declaracao.contribuinte.nome)
        self.pular_campo() # Pula para o OK diretamente

        # Clicar em OK para abrir uma nova declaração
        # Não é necessário apontar para NovaDeclaracao.BOTAO_OK_DECLARACAO_EM_BRANCO porque o direcionamento é automático
        self.pressionar_enter()

        # No caso de uma declaração de ajuste anual, existe um botão de confirmação
        if declaracao.tipo_de_declaracao == TiposDeDeclaracao.AJUSTE_ANUAL:
            self.esperar()
            self.pressionar_enter()

        self.esperar()
        self.esperar()


    @descrever_acao
    def cadastrar_contribuinte(self, declaracao: Declaracao) -> None:
        
        # Apontar para a janela
        self.focar_na_janela_correta()

        # Abrir a ficha de identificação do contrbuinte
        posicao_do_clique = self.mapa_do_sistema.secoes_do_menu_lateral(SecoesDoSistema.SECAO_IDENTIFICACAO_DO_CONTRIBUINTE, declaracao.tipo_de_declaracao)
        self.clicar_na_posicao(posicao_do_clique)

        # Escolher o tipo de declaração
        posicao_do_clique = self.mapa_do_sistema.posicao_na_tela_de_cadastro_de_contribuinte(declaracao.declaracao_retificada, self.tamanho_da_tela)
        self.clicar_na_posicao(posicao_do_clique)
        self.pular_campo()

        # Pular para o segundo campo
        if declaracao.declaracao_retificada == DeclaracaoRetificada.SIM:
            self.escrever_no_campo(declaracao.declaracao_retificada)
        elif declaracao.declaracao_retificada == DeclaracaoRetificada.NAO:
            self.escrever_no_campo(declaracao.numero_do_recibo)
        self.pular_campo()

        # Escrever os dados do contribuinte
        self.escrever_no_campo(declaracao.contribuinte.nome)
        self.pular_campo()

        self.escrever_no_campo(declaracao.contribuinte.data_de_nascimento)
        self.pular_campo()
        
        self.escrever_no_campo(declaracao.contribuinte.titulo_eleitoral)
        self.pular_campo()
        
        if declaracao.contribuinte.pessoa_com_deficiencia == PessoaComDeficiencia.SIM:
            self.pressionar_espaco()
        elif declaracao.contribuinte.pessoa_com_deficiencia == PessoaComDeficiencia.NAO:
            pass
        self.pular_campo()
        
        if declaracao.houve_alteracoes_cadastrais == AlteracoesCadastrais.SIM:
            self.pressionar_espaco()
        elif declaracao.houve_alteracoes_cadastrais == AlteracoesCadastrais.NAO:
            self.setas_a_direita()
            self.pressionar_espaco()
        self.pular_campo()

        if declaracao.contribuinte.possui_conjuge == PossuiConjuge.SIM:
            self.pressionar_espaco()
        elif declaracao.contribuinte.possui_conjuge == PossuiConjuge.NAO:
            self.setas_a_direita()
            self.pressionar_espaco()
        self.pular_campo()

        self.escrever_no_campo(declaracao.contribuinte.cpf_do_conjuge)
        self.pular_campo()

        if declaracao.contribuinte.localizacao_do_endereco == LocalizacaoDoEndereco.BRASIL:
            self.pressionar_espaco()
            self.pular_campo()

            self.escrever_no_campo(declaracao.contribuinte.endereco.tipo_de_logradouro)
            self.pular_campo()

            self.escrever_no_campo(declaracao.contribuinte.endereco.logradouro)
            self.pular_campo()

            self.escrever_no_campo(declaracao.contribuinte.endereco.numero)
            self.pular_campo()

            self.escrever_no_campo(declaracao.contribuinte.endereco.complemento)
            self.pular_campo()

            self.escrever_no_campo(declaracao.contribuinte.endereco.bairro)
            self.pular_campo()

            self.escrever_no_campo(declaracao.contribuinte.endereco.uf)
            self.pular_campo()

            memoria.copy(declaracao.contribuinte.endereco.nome_do_municipio)
            rpa.hotkey('ctrl', 'v')
            self.pular_campo()

            self.escrever_no_campo(declaracao.contribuinte.endereco.cep)
            self.pular_campo()

            self.pular_campo()

            self.escrever_no_campo(declaracao.contribuinte.ddd_telefone)
            self.pular_campo()

            self.escrever_no_campo(declaracao.contribuinte.telefone)
            self.pular_campo()

            self.escrever_no_campo(declaracao.contribuinte.ddd_celular)
            self.pular_campo()

            self.escrever_no_campo(declaracao.contribuinte.celular)
            self.pular_campo()

            self.escrever_no_campo(declaracao.contribuinte.email)
            self.pular_campo()

            self.escrever_no_campo(declaracao.contribuinte.natureza)
            self.pular_campo()
            
            self.escrever_no_campo(declaracao.contribuinte.ocupacao)
            self.pular_campo()


        elif declaracao.contribuinte.localizacao_do_endereco == LocalizacaoDoEndereco.EXTERIOR:
            pass
        self.pular_campo()


    @descrever_acao
    def cadastrar_dependentes(self, declaracao: Declaracao) -> None:
        
        # Apontar para a janela
        self.focar_na_janela_correta()

        quantidade_de_dependentes = len(declaracao.dependentes)

        if quantidade_de_dependentes > 0:

            # Abrir a ficha de identificação do contrbuinte
            posicao_do_clique = self.mapa_do_sistema.secoes_do_menu_lateral(SecoesDoSistema.SECAO_DEPENDENTES, declaracao.tipo_de_declaracao)
            self.clicar_na_posicao(posicao_do_clique)

            for dependente in declaracao.dependentes:

                posicao_do_clique = self.mapa_do_sistema.posicao_na_tela_cadastro_de_dependentes(self.tamanho_da_tela, PosicoesSecaoDependentes.BOTAO_NOVO)
                self.clicar_na_posicao(posicao_do_clique)

                self.escrever_no_campo(str(dependente.tipo_de_dependente.value))
                self.setas_para_baixo()
                self.pressionar_enter()

                self.escrever_no_campo(dependente.cpf)
                self.pular_campo()

                self.escrever_no_campo(dependente.data_de_nascimento)
                self.pular_campo()

                self.escrever_no_campo(dependente.nome)
                self.pular_campo()

                self.escrever_no_campo(dependente.email)
                self.pular_campo()

                self.escrever_no_campo(dependente.ddd)
                self.pular_campo()

                self.escrever_no_campo(dependente.celular)
                self.pular_campo()

                if dependente.saida_do_pais == SaidaDoPais.SIM:
                    self.pressionar_espaco()
                elif dependente.saida_do_pais == SaidaDoPais.NAO:
                    self.setas_a_direita()
                    self.pressionar_espaco()
                    self.pular_campo()
                
                posicao_do_clique = self.mapa_do_sistema.posicao_na_tela_cadastro_de_dependentes(self.tamanho_da_tela, PosicoesSecaoDependentes.BOTAO_OK_CADASTRAR)
                self.clicar_na_posicao(posicao_do_clique)


    @descrever_acao
    def cadastrar_ativos(self, declaracao: Declaracao) -> None:

         # Apontar para a janela
        self.focar_na_janela_correta()

        quantidade_de_imoveis = len(declaracao.bens_e_direitos)

        if quantidade_de_imoveis > 0:
            
            # Abrir a ficha de lancamentos de bens e direitos
            posicao_do_clique = self.mapa_do_sistema.secoes_do_menu_lateral(SecoesDoSistema.SECAO_BENS_E_DIREITOS, declaracao.tipo_de_declaracao)
            self.clicar_na_posicao(posicao_do_clique)

            # Cadastra todos os ativos da empresa escolhendo qual procedimento será feito
            for ativo in declaracao.bens_e_direitos:
                match ativo.grupo:
                    case TiposDeAtivos.BENS_IMOVEIS:
                        self.__cadastrar_imoveis__(ativo)
                    case TiposDeAtivos.BENS_MOVEIS:
                        self.__cadastrar_moveis__(ativo)
                    case TiposDeAtivos.APLICAVOES_E_INVESTIMENTOS:
                        self.__cadastrar_aplicacoes_e_investimentos__(ativo)
                    case TiposDeAtivos.PARTICIPACOES_SOCIETARIAS:
                        self.__cadastrar_participacoes_societarias__(ativo)

    @descrever_acao
    def __cadastrar_imoveis__(self, imovel: Imoveis) -> None:

        posicao_do_clique = self.mapa_do_sistema.posicao_na_tela_cadastro_de_bens_e_direitos(self.tamanho_da_tela, PosicoesSecaoBensEDireitos.BOTAO_NOVO)
        self.clicar_na_posicao(posicao_do_clique)

        self.escrever_no_campo(imovel.grupo.value)
        self.pular_campo()

        self.escrever_no_campo(imovel.codigo.value)
        self.pular_campo()

        # self.escrever_no_campo(imovel.pais) # Não precisa
        self.pular_campo()

        if imovel.codigo == TiposDeImoveis.CONSTRUCAO:
            self.escrever_no_campo(imovel.cei_no)
            self.pular_campo()
        
        elif imovel.codigo == TiposDeImoveis.BENFEITORIAS:
            pass

        else:
            self.escrever_no_campo(imovel.inscricao_municipal)
            self.pular_campo()

            self.escrever_no_campo(imovel.data_de_aquisicao)
            self.pular_campo()


        self.escrever_no_campo(imovel.discriminacao)
        self.pular_campo()

        self.escrever_no_campo((imovel.tipo_de_logradouro + ' ' + imovel.logradouro))
        self.pular_campo()

        self.escrever_no_campo(imovel.numero)
        self.pular_campo()

        self.escrever_no_campo(imovel.complemento)
        self.pular_campo()

        self.escrever_no_campo(imovel.bairro)
        self.pular_campo()

        self.escrever_no_campo(imovel.uf)
        self.pular_campo()

        memoria.copy(imovel.nome_do_municipio)
        rpa.hotkey('ctrl', 'v')
        self.pular_campo()

        self.escrever_no_campo(imovel.cep)
        self.pular_campo()
        self.pular_campo() # Pular o botão do CEP

        self.escrever_no_campo(imovel.area_do_imovel)
        self.pular_campo()

        if imovel.unidade == UnidadeDeMedida.M2:
            self.pressionar_espaco()
        elif imovel.unidade == UnidadeDeMedida.HA:
            self.setas_a_direita()
            self.pressionar_espaco()
            self.pular_campo()

        
        if imovel.codigo == TiposDeImoveis.CONSTRUCAO:
            pass
        
        elif imovel.codigo == TiposDeImoveis.BENFEITORIAS:
            pass

        else:
            if imovel.registro_em_cartorio == RegistroEmCartorio.SIM:
                self.pressionar_espaco()
                self.pular_campo()

                self.escrever_no_campo(imovel.matricula_do_imovel)
                self.pular_campo()

                self.escrever_no_campo(imovel.nome_do_cartorio)
                self.pular_campo()

            elif imovel.registro_em_cartorio == RegistroEmCartorio.NAO:
                self.setas_a_direita()
                self.pressionar_espaco()
                self.pular_campo()


        self.escrever_no_campo(imovel.situacao_ano_anterior)
        self.pressionar_enter()

        self.escrever_no_campo(imovel.situacao_ano_atual)
        self.pressionar_enter()

        # Conclui o cadastro
        posicao_do_clique = self.mapa_do_sistema.posicao_na_tela_cadastro_de_bens_e_direitos(self.tamanho_da_tela, PosicoesSecaoBensEDireitos.BOTAO_OK_CADASTRAR)
        self.clicar_na_posicao(posicao_do_clique)


    def __cadastrar_moveis__(self, bem_movel: BensMoveis) -> None:

        posicao_do_clique = self.mapa_do_sistema.posicao_na_tela_cadastro_de_bens_e_direitos(self.tamanho_da_tela, PosicoesSecaoBensEDireitos.BOTAO_NOVO)
        self.clicar_na_posicao(posicao_do_clique)

        self.escrever_no_campo(bem_movel.grupo.value)
        self.pular_campo()

        self.escrever_no_campo(bem_movel.codigo.value)
        self.pular_campo()

        # self.escrever_no_campo(bem_movel.pais) # Não precisa
        self.pular_campo()

        if bem_movel.codigo == TiposdDeBensMoveis.VEICULO_AUTOMOTOR:
            self.escrever_no_campo(bem_movel.renavam)
            self.pular_campo()
        
        elif bem_movel.codigo == TiposdDeBensMoveis.EMBARCACAO:
            self.escrever_no_campo(bem_movel.registro_de_embarcacao)
            self.pular_campo()
        
        elif bem_movel.codigo == TiposdDeBensMoveis.AERONAVE:
            self.escrever_no_campo(bem_movel.registro_de_embarcacao)
            self.pular_campo()

        self.escrever_no_campo(bem_movel.discriminacao)
        self.pular_campo()

        self.escrever_no_campo(bem_movel.situacao_ano_anterior)
        self.pressionar_enter()

        self.escrever_no_campo(bem_movel.situacao_ano_atual)
        self.pressionar_enter()

        # Conclui o cadastro
        posicao_do_clique = self.mapa_do_sistema.posicao_na_tela_cadastro_de_bens_e_direitos(self.tamanho_da_tela, PosicoesSecaoBensEDireitos.BOTAO_OK_CADASTRAR)
        self.clicar_na_posicao(posicao_do_clique)


    def __cadastrar_aplicacoes_e_investimentos__(self, aplicacoes_e_investimentos: AplicacoesInvestimentos) -> None:
        
        posicao_do_clique = self.mapa_do_sistema.posicao_na_tela_cadastro_de_bens_e_direitos(self.tamanho_da_tela, PosicoesSecaoBensEDireitos.BOTAO_NOVO)
        self.clicar_na_posicao(posicao_do_clique)

        self.escrever_no_campo(aplicacoes_e_investimentos.grupo.value)
        self.pular_campo()

        self.escrever_no_campo(aplicacoes_e_investimentos.codigo.value)
        self.pular_campo()

        try:
            if aplicacoes_e_investimentos.dono_do_ativo == ProprietarioDeUmAtivo.TITULAR:
                self.pressionar_espaco()
            elif aplicacoes_e_investimentos.dono_do_ativo == ProprietarioDeUmAtivo.DEPENDENTE:
                self.setas_a_direita()
                self.pressionar_espaco()
        except:
            pass
        finally:
                self.pular_campo()

        # self.escrever_no_campo(aplicacoes_e_investimentos.pais) # Não precisa
        self.pular_campo()

        if aplicacoes_e_investimentos.codigo == TiposDeAplicacoesInvestimentos.ATIVOS_NEGOCIADOS_EM_BOLSA:
            pass
        elif aplicacoes_e_investimentos.codigo == TiposDeAplicacoesInvestimentos.OURO_ATIVO_FINANCEIRO:
            pass
        else:
            self.escrever_no_campo(aplicacoes_e_investimentos.cnpj_do_ativo)
            self.pular_campo()

        self.escrever_no_campo(aplicacoes_e_investimentos.discriminacao)
        self.pular_campo()

        if aplicacoes_e_investimentos.codigo == TiposDeAplicacoesInvestimentos.DEPOSITOS_EM_CONTA_POUPANCA:

            self.escrever_no_campo(aplicacoes_e_investimentos.codigo_do_banco)
            self.setas_para_baixo()
            self.pressionar_enter()

            self.escrever_no_campo(aplicacoes_e_investimentos.agencia)
            self.pressionar_enter()

            self.escrever_no_campo(aplicacoes_e_investimentos.conta)
            self.pressionar_enter()

            self.escrever_no_campo(aplicacoes_e_investimentos.digito)
            self.pressionar_enter()

        self.escrever_no_campo(aplicacoes_e_investimentos.situacao_ano_anterior)
        self.pressionar_enter()

        self.escrever_no_campo(aplicacoes_e_investimentos.situacao_ano_atual)
        self.pressionar_enter()

        # Conclui o cadastro
        posicao_do_clique = self.mapa_do_sistema.posicao_na_tela_cadastro_de_bens_e_direitos(self.tamanho_da_tela, PosicoesSecaoBensEDireitos.BOTAO_OK_CADASTRAR)
        self.clicar_na_posicao(posicao_do_clique)


    def __cadastrar_participacoes_societarias__(self, participacoes_societarias: ParticipacoesSocietarias) -> None:
        
        posicao_do_clique = self.mapa_do_sistema.posicao_na_tela_cadastro_de_bens_e_direitos(self.tamanho_da_tela, PosicoesSecaoBensEDireitos.BOTAO_NOVO)
        self.clicar_na_posicao(posicao_do_clique)

        self.escrever_no_campo(participacoes_societarias.grupo.value)
        self.pular_campo()

        self.escrever_no_campo(participacoes_societarias.codigo.value)
        self.pular_campo()

        try:
            if participacoes_societarias.dono_do_ativo == ProprietarioDeUmAtivo.TITULAR:
                self.pressionar_espaco()
            elif participacoes_societarias.dono_do_ativo == ProprietarioDeUmAtivo.DEPENDENTE:
                self.setas_a_direita()
                self.pressionar_espaco()
                self.pular_campo()
        except:
            pass

        # self.escrever_no_campo(participacoes_societarias.pais) # Não precisa
        self.pular_campo()

        self.escrever_no_campo(participacoes_societarias.cnpj_do_ativo)
        self.pular_campo()

        self.escrever_no_campo(participacoes_societarias.discriminacao)
        self.pular_campo()

        self.escrever_no_campo(participacoes_societarias.situacao_ano_anterior)
        self.pressionar_enter()

        self.escrever_no_campo(participacoes_societarias.situacao_ano_atual)
        self.pressionar_enter()

        # Conclui o cadastro
        posicao_do_clique = self.mapa_do_sistema.posicao_na_tela_cadastro_de_bens_e_direitos(self.tamanho_da_tela, PosicoesSecaoBensEDireitos.BOTAO_OK_CADASTRAR)
        self.clicar_na_posicao(posicao_do_clique)





