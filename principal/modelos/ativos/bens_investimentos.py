

from principal.modelos.ativos.ativos import Ativos
from principal.modelos.enums.bens_e_direitos import ProprietarioDeUmAtivo, TiposDeAplicacoesInvestimentos, TiposDeAtivos


class AplicacoesInvestimentos(Ativos):

    def __init__(self, grupo: TiposDeAtivos, codigo: TiposDeAplicacoesInvestimentos, pais, codigo_do_banco, cnpj_do_ativo, agencia, conta, digito, dono_do_ativo: ProprietarioDeUmAtivo, discriminacao, situacao_ano_anterior, situacao_ano_atual) -> None:
        self.codigo_do_banco = codigo_do_banco
        self.agencia = agencia
        self.cnpj_do_ativo = cnpj_do_ativo
        self.conta = conta
        self.digito = digito
        self.dono_do_ativo = dono_do_ativo

        Ativos.__init__(self, grupo, codigo, pais, discriminacao, situacao_ano_anterior, situacao_ano_atual)
        