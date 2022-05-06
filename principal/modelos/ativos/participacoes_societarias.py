




from principal.modelos.ativos.ativos import Ativos
from principal.modelos.enums.bens_e_direitos import TiposDeAtivos, TiposDeParticipacoesSocietarias


class ParticipacoesSocietarias(Ativos):

    def __init__(self, grupo: TiposDeAtivos, codigo: TiposDeParticipacoesSocietarias, pais, cnpj_do_ativo, discriminacao, situacao_ano_anterior, situacao_ano_atual) -> None:
        self.cnpj_do_ativo = cnpj_do_ativo


        # Atualizar a classe herdada do ativo
        Ativos.__init__(self, grupo, codigo, pais, discriminacao, situacao_ano_anterior, situacao_ano_atual)
