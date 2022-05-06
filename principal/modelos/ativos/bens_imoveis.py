

from principal.modelos.cadastros.endereco import Endereco
from principal.modelos.enums.bens_e_direitos import TiposDeAtivos, TiposDeImoveis, UnidadeDeMedida, RegistroEmCartorio
from principal.modelos.ativos.ativos import Ativos


class Imoveis(Ativos, Endereco):
    def __init__(self, grupo: TiposDeAtivos, codigo: TiposDeImoveis, pais, cei_no, discriminacao, situacao_ano_anterior, situacao_ano_atual, inscricao_municipal, data_de_aquisicao, tipo_de_logradouro, logradouro, numero, complemento, bairro, uf, nome_do_municipio, cep, area_do_imovel, unidade: UnidadeDeMedida, registro_em_cartorio: RegistroEmCartorio, matricula_do_imovel, nome_do_cartorio) -> None:
        self.inscricao_municipal = inscricao_municipal
        self.data_de_aquisicao = data_de_aquisicao
        self.cei_no = cei_no
        self.area_do_imovel = area_do_imovel
        self.unidade = unidade
        self.registro_em_cartorio = registro_em_cartorio
        self.matricula_do_imovel = matricula_do_imovel
        self.nome_do_cartorio = nome_do_cartorio

        Endereco.__init__(self, tipo_de_logradouro, logradouro, numero, complemento, bairro, uf, nome_do_municipio, cep, pais) 

        # Atualizar a classe herdada do ativo
        Ativos.__init__(self, grupo, codigo, pais, discriminacao, situacao_ano_anterior, situacao_ano_atual)


