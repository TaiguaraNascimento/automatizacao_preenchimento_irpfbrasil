

from principal.modelos.enums.sistema import VersaoDoPrograma


class Mapeamento:

    def titulo_do_sistema_por_versao(self, versao_do_programa: VersaoDoPrograma):
        match versao_do_programa:
            case VersaoDoPrograma.VERSAO_2022:
                return 'IRPF 2022'
            
    def nome_da_instalacao_por_versao(self, versao_do_programa: VersaoDoPrograma):
        match versao_do_programa:
            case VersaoDoPrograma.VERSAO_2022:
                return "IRPF2022 - Declara"