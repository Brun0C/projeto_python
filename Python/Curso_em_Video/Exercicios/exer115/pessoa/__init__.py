def apagar():
    pass


def atualizar():
    print('Cadastrada atualizado')


def cadastrar():
    from uteis import cabecalho, limpar_tela
    
    nome = idade = ''
    while True:
        limpar_tela()
        cabecalho(' Cadastrar Pessoa')
        
        if not nome:
            nome = input('Nome: ').strip()
            if not nome:
                continue
        else:
            print(f'Nome: {nome}')
        
        idade = input('Idade: ').strip()
        if not idade.isdecimal():
            print('\033[31m')
            cabecalho('ERRO!!! Insira somente números.', 1.5)
            print('\033[m')
            input('Pressione ENTER para continuar...')
            continue
        idade = int(idade)
        break
        
    print('\nPessoa cadastrada\n')
    input('Pressione ENTER para continuar...')


def listar():
    pass

