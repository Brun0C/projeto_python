'''
Lista os módulos para criação dos menus do programa.
'''

def menu_principal():
    '''
    Modulo que retorna uma tupla contendo o titulo e as opções para criar o Menu Principal.
    '''
    titulo = 'Menu Principal'
    opcoes = {
        'Cadastrar pessoa': 'pessoa',
        'Listar pessoas cadastradas': 'pessoa.pessoa'
    }
    return titulo, opcoes
    
    
