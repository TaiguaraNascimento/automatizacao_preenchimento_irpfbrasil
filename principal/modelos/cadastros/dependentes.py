

from principal.modelos.enums.contribuinte import SaidaDoPais, TipoDeDependente


class Dependentes:

    def __init__(self, tipo_de_dependente: TipoDeDependente, cpf, data_de_nascimento, nome, email, ddd, celular, saida_do_pais: SaidaDoPais) -> None:
        self.tipo_de_dependente = tipo_de_dependente 
        self.cpf = cpf 
        self.data_de_nascimento = data_de_nascimento 
        self.nome = nome 
        self.email = email 
        self.ddd = ddd 
        self.celular = celular 
        self.saida_do_pais = saida_do_pais 