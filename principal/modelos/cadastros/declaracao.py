from principal.modelos.ativos.ativos import Ativos
from principal.modelos.cadastros.contribuinte import Contribuinte
from principal.modelos.cadastros.dependentes import Dependentes
from principal.modelos.enums.contribuinte import AlteracoesCadastrais, DeclaracaoRetificada, TiposDeDeclaracao

class Declaracao:
    """A classe Declaração representa uma nova declaração dentro do imposto de renda pessoa física. """
    def __init__(self, nome: str, cpf: str, data_de_nascimento: str, tipo_de_declaracao: TiposDeDeclaracao, numero_do_recibo: str, declaracao_retificada: DeclaracaoRetificada, houve_alteracoes_cadastrais: AlteracoesCadastrais) -> None:
        self.contribuinte = Contribuinte()
        self.contribuinte.definir_dados_pessoais(nome, cpf, data_de_nascimento)
        self.tipo_de_declaracao = tipo_de_declaracao
        self.numero_do_recibo = numero_do_recibo
        self.declaracao_retificada = declaracao_retificada
        self.houve_alteracoes_cadastrais = houve_alteracoes_cadastrais 
        self.dependentes = []
        self.bens_e_direitos = []


    def adicionar_dependente(self, dependente: Dependentes) -> None:
        self.dependentes.append(dependente)

    
    def adicionar_bens_e_direitos(self, ativos: Ativos) -> None:
        self.bens_e_direitos.append(ativos)

        
    