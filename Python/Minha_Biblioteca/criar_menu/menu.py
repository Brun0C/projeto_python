def exibir_menu(titulo: str, opcoes: dict):
    
    from sys import platform
    from IPython.display import clear_output as cls_out
    import os
    
    tamanho_título = len(titulo) + 25
    while True:
        cls_out(wait=True)
        
        if platform == "linux" or platform == "linux2":
            # linux
            os.system('clear')
        elif platform == "win32":
            # Windows...
            #os.system('pause')
            os.system('cls')
        
        print(
            '=' * tamanho_título,
            titulo.upper().center(tamanho_título),
            '=' * tamanho_título,
            sep = '\n'
        )
        for indice, opcao in enumerate(opcoes, 1):
            print(f'[{indice}] - {opcao}')
        print('\n[0] - Sair')
        op = str(input('\nEscolha uma opção: ')).strip()
        if op.isdecimal():
            if int(op) == 0:
                break
            elif 0 < int(op) <= len(opcoes):
                funcao = list(opcoes.values())[int(op) - 1]
                return funcao
        
        print('ERROR!!! Opção inválida.')
        input('Pressione ENTER para continua...')
        
