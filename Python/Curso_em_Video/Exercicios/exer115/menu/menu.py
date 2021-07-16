def exibir_menu(titulo, opcoes):
    '''
    --> Cria um menu interativo retornando a opção escolhida.
    :param titulo: string para exibir nome dado ao menu.
    :param opcoes: dicionario de opções para exibir no menu, 
                    onde a chave é o nome da opção e o valor
                    caminho para chamar a função.
    :return: retorna o valor do dicionario, escolhido nas opções do menu.
    '''
    
    from uteis import limpar_tela, cabecalho
    
    while True:
        
        cabecalho(titulo)
        
        for indice, opcao in enumerate(opcoes, 1):
            print(f'\033[33m[{indice}] - \033[34m{opcao}\033[m')
        print('\n\033[33m[0] - \033[34mSair\033[m\n')
        
        op = str(input('Escolha uma opção: ')).strip()
        
        if op.isdecimal():
            if int(op) == 0:
                print('Saindo do sistema...')
                break
            elif 0 < int(op) <= len(opcoes):
                funcao = list(opcoes.values())[int(op) - 1]
                return funcao

        print('\033[31m')
        cabecalho('ERRO!!! Opção inválida.', 2)
        print('\033[m' )
        input('Pressione ENTER para continuar...')
        limpar_tela()
        