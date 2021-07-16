def limpar_tela():
    
    '''
    Limpa todo o conteúdo do console do Jupyter Notebook e do terminar (Prompt).
    '''
    
    from IPython.display import clear_output as cls_out
    from sys import platform
    import os
    
    def no_terminal():

        '''
        Limpa todo o conteúdo do terminal (Prompt).
        '''

        if platform == "linux" or platform == "linux2":
            # linux
            os.system('clear')
        elif platform == "win32":
            # Windows...
            os.system('cls')


    def no_jupyter():

        '''
        Limpa todo o conteúdo do console do Jupyter Notebook.
        '''
        
        cls_out(wait=True)
        
        
    no_terminal()
    no_jupyter()
    
    
def cabecalho(msg: str, num: int = 3):
    '''
    --> Formata uma mensagem colocando-a dentro de uma moldura.
    :param msg: string para exibir nome dado ao menu.
    :param opcoes: dicionario de opções para exibir no menu, 
                    onde a chave é o nome da opção e o valor
                    caminho para chamar a função.
    :return: retorna o valor do dicionario, escolhido nas opções do menu.
    '''
    
    tamanho_msg = int(len(msg) * num + 2)
        
    print(
        '=' * tamanho_msg,
        f'|{msg.upper().center(tamanho_msg-2)}|',
        '=' * tamanho_msg,
        sep = '\n'
    )
    
    