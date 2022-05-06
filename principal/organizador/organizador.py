import os



class Organizador:

    def __init__(self) -> None:
        self.nome_da_pasta_base = 'GMS_Processamento'
        pass


    def organizar_pasta_endereco_base(self):
        print(self.__obter_nome_do_endereco_de_organizacao__())


    def __obter_nome_do_endereco_de_organizacao__(self):

        endereco_de_organizacao = self.__obter_endereco_da_pasta_desktop__()
        if endereco_de_organizacao == None or len(endereco_de_organizacao) == 0:
            return 'C:\\' + self.nome_da_pasta_base + '\\'
        else:
            return endereco_de_organizacao


    def __obter_endereco_da_pasta_desktop__(self):
        try:
            return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') + '\\'
        except:
            return ''