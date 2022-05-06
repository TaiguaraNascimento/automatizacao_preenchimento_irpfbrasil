from principal.modelos.ativos.bens_imoveis import Imoveis
from principal.modelos.ativos.bens_investimentos import AplicacoesInvestimentos
from principal.modelos.ativos.bens_moveis import BensMoveis
from principal.modelos.ativos.participacoes_societarias import ParticipacoesSocietarias
from principal.modelos.cadastros.declaracao import Declaracao
from principal.modelos.cadastros.dependentes import Dependentes
from principal.modelos.enums.bens_e_direitos import ProprietarioDeUmAtivo, TiposDeAplicacoesInvestimentos, TiposDeAtivos, TiposDeImoveis, TiposDeParticipacoesSocietarias, TiposdDeBensMoveis, UnidadeDeMedida, RegistroEmCartorio
from principal.modelos.enums.contribuinte import AlteracoesCadastrais, DeclaracaoRetificada, LocalizacaoDoEndereco, PessoaComDeficiencia, PossuiConjuge, SaidaDoPais, TipoDeDependente, TiposDeDeclaracao


class DeclaracaoFactory:

    def __init__(self, endereco_do_arquivo: str) -> None:
        self.endereco_do_arquivo = endereco_do_arquivo

    def obter_declaracao_a_partir_do_arquivo(self) -> Declaracao:
        declaracao = Declaracao('Taiguara Nascimento', '33321464837', '29/04/1986', TiposDeDeclaracao.SAIDA_DEFINITIVA, '2135464646', DeclaracaoRetificada.NAO, AlteracoesCadastrais.NAO)
        declaracao.contribuinte.definir_documentos('12345678910')
        declaracao.contribuinte.definir_endereco(LocalizacaoDoEndereco.BRASIL, 'Rua', 'Carlos Grotte', '152', 'Não possui complemento', 'Jd Vila Sonia', 'SP', 'Taboão da Serra', '06765460', 'Brasil')
        declaracao.contribuinte.definir_conjuge(PossuiConjuge.SIM, '05293601873')
        declaracao.contribuinte.definir_ocupacao('02', '900')
        declaracao.contribuinte.definir_condicoes_fisicas(PessoaComDeficiencia.SIM)
        declaracao.contribuinte.definir_contatos('19', '47875810', '11', '79571212', 'taiguara@uol.com')

        # self.adicionar_dependentes_a_declaracao(declaracao)
        
        # self.adicionar_imoveis_a_declaracao(declaracao)

        # self.adicionar_bens_moveis_a_declaracao(declaracao)

        self.adicionar_aplicacoes_e_investimentos(declaracao)

        # self.adicionar_participacoes_societarias(declaracao)

        return declaracao
    

    def adicionar_imoveis_a_declaracao(self, declaracao: Declaracao) -> None:
        declaracao.adicionar_bens_e_direitos(Imoveis(TiposDeAtivos.BENS_IMOVEIS, TiposDeImoveis.BENFEITORIAS,  '105', '125468497987', 'APARTAMENTO À RUA CARLOS GROTTE, 152 - JD VILA SONIA - TABOÃO', '125035,74', '150332,12', '112225222', '29/04/1986', 'Rua', 'Carlos Grotte', '152', 'N/A', 'JD Vila Sonia', 'SP', 'Taboão da Serra', '06765460', '125', UnidadeDeMedida.HA, RegistroEmCartorio.SIM, '7967', '2 TABELIONATO'))
        declaracao.adicionar_bens_e_direitos(Imoveis(TiposDeAtivos.BENS_IMOVEIS, TiposDeImoveis.PREDIO_COMERCIAL,  '105', '01.011.11212/21', 'APARTAMENTO À RUA CARLOS GROTTE, 152 - JD VILA SONIA - TABOÃO', '125035,74', '150332,12', '112225222', '29/04/1986', 'Rua', 'Carlos Grotte', '152', 'N/A', 'JD Vila Sonia', 'SP', 'Taboão da Serra', '06765460', '125', UnidadeDeMedida.HA, RegistroEmCartorio.SIM, '7967', '2 TABELIONATO'))
        declaracao.adicionar_bens_e_direitos(Imoveis(TiposDeAtivos.BENS_IMOVEIS, TiposDeImoveis.PREDIO_RESIDENCIAL,  '105', '01.011.11212/21', 'APARTAMENTO À RUA CARLOS GROTTE, 152 - JD VILA SONIA - TABOÃO', '125035,74', '150332,12', '112225222', '29/04/1986', 'Rua', 'Carlos Grotte', '152', 'N/A', 'JD Vila Sonia', 'SP', 'Taboão da Serra', '06765460', '125', UnidadeDeMedida.HA, RegistroEmCartorio.SIM, '7967', '2 TABELIONATO'))
        declaracao.adicionar_bens_e_direitos(Imoveis(TiposDeAtivos.BENS_IMOVEIS, TiposDeImoveis.GALPAO,  '105', '01.011.11212/21', 'APARTAMENTO À RUA CARLOS GROTTE, 152 - JD VILA SONIA - TABOÃO', '125035,74', '150332,12', '112225222', '29/04/1986', 'Rua', 'Carlos Grotte', '152', 'N/A', 'JD Vila Sonia', 'SP', 'Taboão da Serra', '06765460', '125', UnidadeDeMedida.HA, RegistroEmCartorio.SIM, '7967', '2 TABELIONATO'))
        declaracao.adicionar_bens_e_direitos(Imoveis(TiposDeAtivos.BENS_IMOVEIS, TiposDeImoveis.CASA,  '105', '01.011.11212/21', 'APARTAMENTO À RUA CARLOS GROTTE, 152 - JD VILA SONIA - TABOÃO', '125035,74', '150332,12', '112225222', '29/04/1986', 'Rua', 'Carlos Grotte', '152', 'N/A', 'JD Vila Sonia', 'SP', 'Taboão da Serra', '06765460', '125', UnidadeDeMedida.HA, RegistroEmCartorio.SIM, '7967', '2 TABELIONATO'))
        declaracao.adicionar_bens_e_direitos(Imoveis(TiposDeAtivos.BENS_IMOVEIS, TiposDeImoveis.TERRENO,  '105', '01.011.11212/21', 'APARTAMENTO À RUA CARLOS GROTTE, 152 - JD VILA SONIA - TABOÃO', '125035,74', '150332,12', '112225222', '29/04/1986', 'Rua', 'Carlos Grotte', '152', 'N/A', 'JD Vila Sonia', 'SP', 'Taboão da Serra', '06765460', '125', UnidadeDeMedida.HA, RegistroEmCartorio.SIM, '7967', '2 TABELIONATO'))
        declaracao.adicionar_bens_e_direitos(Imoveis(TiposDeAtivos.BENS_IMOVEIS, TiposDeImoveis.IMOVEL_RURAL,  '105', '01.011.11212/21', 'APARTAMENTO À RUA CARLOS GROTTE, 152 - JD VILA SONIA - TABOÃO', '125035,74', '150332,12', '112225222', '29/04/1986', 'Rua', 'Carlos Grotte', '152', 'N/A', 'JD Vila Sonia', 'SP', 'Taboão da Serra', '06765460', '125', UnidadeDeMedida.HA, RegistroEmCartorio.SIM, '7967', '2 TABELIONATO'))
        declaracao.adicionar_bens_e_direitos(Imoveis(TiposDeAtivos.BENS_IMOVEIS, TiposDeImoveis.SALA_OU_CONJUNTO,  '105', '01.011.11212/21', 'APARTAMENTO À RUA CARLOS GROTTE, 152 - JD VILA SONIA - TABOÃO', '125035,74', '150332,12', '112225222', '29/04/1986', 'Rua', 'Carlos Grotte', '152', 'N/A', 'JD Vila Sonia', 'SP', 'Taboão da Serra', '06765460', '125', UnidadeDeMedida.HA, RegistroEmCartorio.SIM, '7967', '2 TABELIONATO'))      
        declaracao.adicionar_bens_e_direitos(Imoveis(TiposDeAtivos.BENS_IMOVEIS, TiposDeImoveis.BENFEITORIAS,  '105', '01.011.11212/21', 'APARTAMENTO À RUA CARLOS GROTTE, 152 - JD VILA SONIA - TABOÃO', '125035,74', '150332,12', '112225222', '29/04/1986', 'Rua', 'Carlos Grotte', '152', 'N/A', 'JD Vila Sonia', 'SP', 'Taboão da Serra', '06765460', '125', UnidadeDeMedida.HA, RegistroEmCartorio.SIM, '7967', '2 TABELIONATO'))
        declaracao.adicionar_bens_e_direitos(Imoveis(TiposDeAtivos.BENS_IMOVEIS, TiposDeImoveis.LOJA,  '105', '01.011.11212/21', 'APARTAMENTO À RUA CARLOS GROTTE, 152 - JD VILA SONIA - TABOÃO', '125035,74', '150332,12', '112225222', '29/04/1986', 'Rua', 'Carlos Grotte', '152', 'N/A', 'JD Vila Sonia', 'SP', 'Taboão da Serra', '06765460', '125', UnidadeDeMedida.HA, RegistroEmCartorio.SIM, '7967', '2 TABELIONATO'))
        declaracao.adicionar_bens_e_direitos(Imoveis(TiposDeAtivos.BENS_IMOVEIS, TiposDeImoveis.OUTROS_BENS,  '105', '01.011.11212/21', 'APARTAMENTO À RUA CARLOS GROTTE, 152 - JD VILA SONIA - TABOÃO', '125035,74', '150332,12', '112225222', '29/04/1986', 'Rua', 'Carlos Grotte', '152', 'N/A', 'JD Vila Sonia', 'SP', 'Taboão da Serra', '06765460', '125', UnidadeDeMedida.HA, RegistroEmCartorio.SIM, '7967', '2 TABELIONATO'))
        declaracao.adicionar_bens_e_direitos(Imoveis(TiposDeAtivos.BENS_IMOVEIS, TiposDeImoveis.CONSTRUCAO,  '105', '125468497987', 'APARTAMENTO À RUA CARLOS GROTTE, 152 - JD VILA SONIA - TABOÃO', '125035,74', '150332,12', '112225222', '29/04/1986', 'Rua', 'Carlos Grotte', '152', 'N/A', 'JD Vila Sonia', 'SP', 'Taboão da Serra', '06765460', '125', UnidadeDeMedida.HA, RegistroEmCartorio.SIM, '7967', '2 TABELIONATO'))
        declaracao.adicionar_bens_e_direitos(Imoveis(TiposDeAtivos.BENS_IMOVEIS, TiposDeImoveis.CONSTRUCAO,  '105', '125468497987', 'APARTAMENTO À RUA CARLOS GROTTE, 152 - JD VILA SONIA - TABOÃO', '125035,74', '150332,12', '112225222', '29/04/1986', 'Rua', 'Carlos Grotte', '152', 'N/A', 'JD Vila Sonia', 'SP', 'Taboão da Serra', '06765460', '125', UnidadeDeMedida.HA, RegistroEmCartorio.SIM, '7967', '2 TABELIONATO'))
        declaracao.adicionar_bens_e_direitos(Imoveis(TiposDeAtivos.BENS_IMOVEIS, TiposDeImoveis.CONSTRUCAO,  '105', '125468497987', 'APARTAMENTO À RUA CARLOS GROTTE, 152 - JD VILA SONIA - TABOÃO', '125035,74', '150332,12', '112225222', '29/04/1986', 'Rua', 'Carlos Grotte', '152', 'N/A', 'JD Vila Sonia', 'SP', 'Taboão da Serra', '06765460', '125', UnidadeDeMedida.HA, RegistroEmCartorio.SIM, '7967', '2 TABELIONATO'))
        declaracao.adicionar_bens_e_direitos(Imoveis(TiposDeAtivos.BENS_IMOVEIS, TiposDeImoveis.CONSTRUCAO,  '105', '125468497987', 'APARTAMENTO À RUA CARLOS GROTTE, 152 - JD VILA SONIA - TABOÃO', '125035,74', '150332,12', '112225222', '29/04/1986', 'Rua', 'Carlos Grotte', '152', 'N/A', 'JD Vila Sonia', 'SP', 'Taboão da Serra', '06765460', '125', UnidadeDeMedida.HA, RegistroEmCartorio.SIM, '7967', '2 TABELIONATO'))


    def adicionar_bens_moveis_a_declaracao(self, declaracao: Declaracao) -> None:
        declaracao.adicionar_bens_e_direitos(BensMoveis(TiposDeAtivos.BENS_MOVEIS, TiposdDeBensMoveis.AERONAVE, '12065478', '7487897', '44454587', '105', 'aeronave de teste para declaracao', '2145748,41', '3145781,21'))
        declaracao.adicionar_bens_e_direitos(BensMoveis(TiposDeAtivos.BENS_MOVEIS, TiposdDeBensMoveis.VEICULO_AUTOMOTOR, '12065478', '7487897', '44454587', '105', 'aeronave de teste para declaracao', '2145748,41', '3145781,21'))
        declaracao.adicionar_bens_e_direitos(BensMoveis(TiposDeAtivos.BENS_MOVEIS, TiposdDeBensMoveis.EMBARCACAO, '12065478', '7487897', '44454587', '105', 'aeronave de teste para declaracao', '2145748,41', '3145781,21'))
        declaracao.adicionar_bens_e_direitos(BensMoveis(TiposDeAtivos.BENS_MOVEIS, TiposdDeBensMoveis.BENS_DE_ATIVIDADE_AUTONOMA, '12065478', '7487897', '44454587', '105', 'aeronave de teste para declaracao', '2145748,41', '3145781,21'))
        declaracao.adicionar_bens_e_direitos(BensMoveis(TiposDeAtivos.BENS_MOVEIS, TiposdDeBensMoveis.JOIAS_ARTES_ETC, '12065478', '7487897', '44454587', '105', 'aeronave de teste para declaracao', '2145748,41', '3145781,21'))
        declaracao.adicionar_bens_e_direitos(BensMoveis(TiposDeAtivos.BENS_MOVEIS, TiposdDeBensMoveis.OUTROS_BENS_MOVEIS, '12065478', '7487897', '44454587', '105', 'aeronave de teste para declaracao', '2145748,41', '3145781,21'))
        declaracao.adicionar_bens_e_direitos(BensMoveis(TiposDeAtivos.BENS_MOVEIS, TiposdDeBensMoveis.AERONAVE, '12065478', '7487897', '44454587', '105', 'aeronave de teste para declaracao', '2145748,41', '3145781,21'))
        declaracao.adicionar_bens_e_direitos(BensMoveis(TiposDeAtivos.BENS_MOVEIS, TiposdDeBensMoveis.AERONAVE, '12065478', '7487897', '44454587', '105', 'aeronave de teste para declaracao', '2145748,41', '3145781,21'))


    def adicionar_dependentes_a_declaracao(self, declaracao: Declaracao) -> None:
        declaracao.adicionar_dependente(Dependentes(TipoDeDependente.FILHO_ENTEADO_ATE_21_ANOS, '05293601873', '06/12/1957', 'Tania Regina Rodrigues do Nascimento', 'tania.e.rosival@gmail.com', '11', '47875810', SaidaDoPais.NAO))
        declaracao.adicionar_dependente(Dependentes(TipoDeDependente.FILHO_ENTEADO_ATE_21_ANOS, '05293601873', '06/12/1957', 'Tania Regina Rodrigues do Nascimento', 'tania.e.rosival@gmail.com', '11', '47875810', SaidaDoPais.NAO))
        declaracao.adicionar_dependente(Dependentes(TipoDeDependente.FILHO_ENTEADO_ATE_21_ANOS, '05293601873', '06/12/1957', 'Tania Regina Rodrigues do Nascimento', 'tania.e.rosival@gmail.com', '11', '47875810', SaidaDoPais.NAO))
        declaracao.adicionar_dependente(Dependentes(TipoDeDependente.FILHO_ENTEADO_ATE_21_ANOS, '05293601873', '06/12/1957', 'Tania Regina Rodrigues do Nascimento', 'tania.e.rosival@gmail.com', '11', '47875810', SaidaDoPais.NAO))
        declaracao.adicionar_dependente(Dependentes(TipoDeDependente.PAIS_AVOS_BISAVOS, '33321464837', '29/04/1986', 'Rubens Pires do Nascimento', 'taiguarapires@gmail.com', '11', '48431682',  SaidaDoPais.SIM))
        declaracao.adicionar_dependente(Dependentes(TipoDeDependente.PAIS_AVOS_BISAVOS, '33321464837', '29/04/1986', 'Rubens Pires do Nascimento', 'taiguarapires@gmail.com', '11', '48431682',  SaidaDoPais.SIM))
        declaracao.adicionar_dependente(Dependentes(TipoDeDependente.PAIS_AVOS_BISAVOS, '33321464837', '29/04/1986', 'Rubens Pires do Nascimento', 'taiguarapires@gmail.com', '11', '48431682',  SaidaDoPais.SIM))
        declaracao.adicionar_dependente(Dependentes(TipoDeDependente.PAIS_AVOS_BISAVOS, '33321464837', '29/04/1986', 'Rubens Pires do Nascimento', 'taiguarapires@gmail.com', '11', '48431682',  SaidaDoPais.SIM))
        declaracao.adicionar_dependente(Dependentes(TipoDeDependente.PAIS_AVOS_BISAVOS, '33321464837', '29/04/1986', 'Rubens Pires do Nascimento', 'taiguarapires@gmail.com', '11', '48431682',  SaidaDoPais.SIM))


    def adicionar_participacoes_societarias(self, declaracao: Declaracao) -> None:
        declaracao.adicionar_bens_e_direitos(ParticipacoesSocietarias(TiposDeAtivos.PARTICIPACOES_SOCIETARIAS, TiposDeParticipacoesSocietarias.ACOES, '105', '60701190000104', 'participação societária em ações da empresa xpto', '12454,39', '54545,12'))
        declaracao.adicionar_bens_e_direitos(ParticipacoesSocietarias(TiposDeAtivos.PARTICIPACOES_SOCIETARIAS, TiposDeParticipacoesSocietarias.OUTRAS_PARTICIPACOES, '105', '60701190000104', 'participação societária em ações da empresa xpto', '12454,39', '54545,12'))
        declaracao.adicionar_bens_e_direitos(ParticipacoesSocietarias(TiposDeAtivos.PARTICIPACOES_SOCIETARIAS, TiposDeParticipacoesSocietarias.QUOTAS_OU_QUINHOES_DE_CAPITAL, '105', '60701190000104', 'participação societária em ações da empresa xpto', '12454,39', '54545,12'))
        declaracao.adicionar_bens_e_direitos(ParticipacoesSocietarias(TiposDeAtivos.PARTICIPACOES_SOCIETARIAS, TiposDeParticipacoesSocietarias.QUOTAS_OU_QUINHOES_DE_CAPITAL, '105', '60701190000104', 'participação societária em ações da empresa xpto', '12454,39', '54545,12'))
        declaracao.adicionar_bens_e_direitos(ParticipacoesSocietarias(TiposDeAtivos.PARTICIPACOES_SOCIETARIAS, TiposDeParticipacoesSocietarias.ACOES, '105', '60701190000104', 'participação societária em ações da empresa xpto', '12454,39', '54545,12'))
        declaracao.adicionar_bens_e_direitos(ParticipacoesSocietarias(TiposDeAtivos.PARTICIPACOES_SOCIETARIAS, TiposDeParticipacoesSocietarias.OUTRAS_PARTICIPACOES, '105', '60701190000104', 'participação societária em ações da empresa xpto', '12454,39', '54545,12'))


    def adicionar_aplicacoes_e_investimentos(self, declaracao: Declaracao) -> None:
       declaracao.adicionar_bens_e_direitos(AplicacoesInvestimentos(TiposDeAtivos.APLICAVOES_E_INVESTIMENTOS, TiposDeAplicacoesInvestimentos.DEPOSITOS_EM_CONTA_POUPANCA, '105', '341', '60701190000104', '6874', '09300', '5', ProprietarioDeUmAtivo.DEPENDENTE, 'CONTA CORRENTE NO BANCO X AVALIADO EM XRPT', '1245,97', '13284,12' ))
       declaracao.adicionar_bens_e_direitos(AplicacoesInvestimentos(TiposDeAtivos.APLICAVOES_E_INVESTIMENTOS, TiposDeAplicacoesInvestimentos.DEPOSITOS_EM_CONTA_POUPANCA, '105', '341', '60701190000104', '6874', '09300', '5', ProprietarioDeUmAtivo.DEPENDENTE, 'CONTA CORRENTE NO BANCO X AVALIADO EM XRPT', '1245,97', '13284,12' ))
       declaracao.adicionar_bens_e_direitos(AplicacoesInvestimentos(TiposDeAtivos.APLICAVOES_E_INVESTIMENTOS, TiposDeAplicacoesInvestimentos.DEPOSITOS_EM_CONTA_POUPANCA, '105', '341', '60701190000104', '6874', '09300', '5', ProprietarioDeUmAtivo.DEPENDENTE, 'CONTA CORRENTE NO BANCO X AVALIADO EM XRPT', '1245,97', '13284,12' ))
       declaracao.adicionar_bens_e_direitos(AplicacoesInvestimentos(TiposDeAtivos.APLICAVOES_E_INVESTIMENTOS, TiposDeAplicacoesInvestimentos.DEPOSITOS_EM_CONTA_POUPANCA, '105', '341', '60701190000104', '6874', '09300', '5', ProprietarioDeUmAtivo.DEPENDENTE, 'CONTA CORRENTE NO BANCO X AVALIADO EM XRPT', '1245,97', '13284,12' ))
       
       


