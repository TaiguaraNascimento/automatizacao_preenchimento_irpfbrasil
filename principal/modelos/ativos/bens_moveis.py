

from principal.modelos.ativos.ativos import Ativos
from principal.modelos.cadastros.endereco import Endereco
from principal.modelos.enums.bens_e_direitos import TiposDeAtivos, TiposdDeBensMoveis


class BensMoveis(Ativos):
    def __init__(self, grupo: TiposDeAtivos, codigo: TiposdDeBensMoveis, renavam, registro_de_aeronave, registro_de_embarcacao, pais, discriminacao, situacao_ano_anterior, situacao_ano_atual) -> None:
        self.renavam = renavam
        self.registro_de_aeronave = registro_de_aeronave
        self.registro_de_embarcacao = registro_de_embarcacao

        # Atualizar a classe herdada do ativo
        Ativos.__init__(self, grupo, codigo, pais, discriminacao, situacao_ano_anterior, situacao_ano_atual)
