from principal.modelos.cadastros.endereco import Endereco


class Contribuinte():
    """A classe contribuinte representa o conjunto de campos referente à pessoa sobre a qual será feita a declaração do imposto de renda. """

    def __init__(self) -> None:
        """Constutor vazio."""
        pass
        
    def definir_dados_pessoais(self,  nome, cpf, data_de_nascimento) -> None:
        """O construtor inicia a classe com informações básicas do contribuinte. """
        self.nome = nome
        self.cpf = cpf
        self.data_de_nascimento = data_de_nascimento
        

    def definir_endereco(self, localizacao_do_endereco, tipo_de_logradouro, logradouro, numero, complemento, bairro, uf, nome_do_municipio, cep, pais) -> None:
        """O método define os dados de endereço do contribuinte. """
        self.endereco = Endereco(tipo_de_logradouro, logradouro, numero, complemento, bairro, uf, nome_do_municipio, cep, pais)
        self.localizacao_do_endereco = localizacao_do_endereco


    def definir_contatos(self, ddd_telefone, telefone, ddd_celular, celular, email) -> None:
        """O método define as informações sobre contato do contribuinte. """

        self.ddd_telefone = ddd_telefone
        self.telefone = telefone
        self.ddd_celular = ddd_celular
        self.celular = celular
        self.email = email


    def definir_documentos(self, titulo_eleitoral):
        self.titulo_eleitoral = titulo_eleitoral


    def definir_conjuge(self, possui_conjuge, cpf_do_conjuge) -> None:
        self.possui_conjuge = possui_conjuge
        self.cpf_do_conjuge = cpf_do_conjuge


    def definir_ocupacao(self, natureza, ocupacao) -> None:
        self.natureza = natureza
        self.ocupacao = ocupacao


    def definir_condicoes_fisicas(self, pessoa_com_deficiencia):
        self.pessoa_com_deficiencia = pessoa_com_deficiencia 