import os
from xmlrpc.client import Boolean
import PySimpleGUI as gui


class Principal:

    nome_do_programa = "Grant Thornton Brasil - GMS IRPF"

    titulo_da_janela = nome_do_programa + ' - ' + 'Automatização do Preenchimento do IRPF'

    def __init__(self) -> None:
        layout_principal = [
            [gui.Text('Essa é a ferramenta de preenchimento automático da Declaração de Ajuste Anual do IRPF da Grant Thornton.')],
            [gui.Text('Para iniciar o processamento, selecione um arquivo pelo botão abaixo e clique em Processar.')],
            [gui.Text('Endereço do arquivo a ser processado:')],
            [gui.Text("Selecione um arquivo: "), gui.In(readonly=True, size=(80,3), key="endereco_do_arquivo"), gui.FileBrowse(file_types=(("Excel Files", "*.xlsx"),))],
            [gui.Text('')],
            [gui.Button('Processar Arquivo', key='processar')]
        ]
    
        self.janela = gui.Window(title=self.titulo_da_janela, margins=(70,30), layout=layout_principal)
        
        self.button, self.values = self.janela.Read()

    def abrir_janela_principal(self) -> None:
        while True:
            event, values = self.janela.read()
            if event == gui.WIN_CLOSED:
                print('Fechou a janela principal.')
                break
            elif event == 'processar':
                
                endereco_do_arquivo = values["endereco_do_arquivo"]

                if self.verificar_se_o_arquivo_existe(endereco_do_arquivo):
                    print('Iniciou o processamento do arquivo: ' + endereco_do_arquivo)
                else:
                    gui.MsgBox("O arquivo selecionado não é válido ou não existe!")
                break

    
    def verificar_se_o_arquivo_existe(self, endereco_do_arquivo) -> Boolean:
        try:
            return os.path.exists(endereco_do_arquivo)
        except:
            return False
                
