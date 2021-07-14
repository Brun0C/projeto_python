'''
Módulos contendo os dados para criação dos menus do programa.
'''

def menu_principal():
    '''
    Modulo que retorna uma tupla contendo o titulo e as opções para criar o Menu Principal.
    '''
    
    import pessoa
    
    titulo = 'Menu Principal'
    opcoes = {
        'Cadastrar pessoa': pessoa.cadastrar,
        'Listar pessoas cadastradas': pessoa.listar,
        'Menu Pessoa': menu_pessoa
    }
    return titulo, opcoes


def menu_pessoa():
    '''
    Modulo que retorna uma tupla contendo o titulo e as opções para criar o Menu Principal.
    '''

    import pessoa

    titulo = 'Menu Pessoa'
    opcoes = {
        'Cadastrar pessoa': pessoa.cadastrar,
        'Listar pessoas cadastradas': pessoa.listar
    }
    return titulo, opcoes   
    
