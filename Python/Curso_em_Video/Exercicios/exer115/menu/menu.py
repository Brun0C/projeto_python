def exibir_menu(titulo, opcoes):
    '''
    --> Cria um menu interativo retornando a opção escolhida.
    :param titulo: string para exibir nome dado ao menu.
    :param opcoes: dicionario de opções para exibir no menu, 
                    onde a chave é o nome da opção e o valor
                    caminho para chamar a função.
    :return: retorna o valor do dicionario, escolhido nas opções do menu.
    '''
    
    from sys import platform
    from IPython.display import clear_output as cls_out
    import os
    
    tamanho_título = len(titulo) * 3
    while True:
        cls_out(wait=True)
        print(
            '=' * tamanho_título,
            titulo.upper().center(tamanho_título),
            '=' * tamanho_título,
            sep = '\n'
        )
        
        for indice, opcao in enumerate(opcoes, 1):
            print(f'\033[33m[{indice}] - \033[34m{opcao}\033[m')
        print('\n\033[33m[0] - \033[34mSair\n')
        
        op = str(input('Escolha uma opção: ')).strip()
        
        if op.isdecimal():
            if int(op) == 0:
                print('Saindo do sistema...')
                break
            elif 0 < int(op) <= len(opcoes):
                funcao = list(opcoes.values())[int(op) - 1]
                return funcao

        print('\033[31mERROR!!! Opção inválida.\033[m')
        
        if platform == "linux" or platform == "linux2":
            # linux
            input('Pressione ENTER para continuar...')
            os.system('clear')
        elif platform == "win32":
            # Windows...
            os.system('pause')
            os.system('cls')
        else:
            input('Pressione ENTER para continuar...')
        
        
