import clientes, funcionarios, pessoas

def menu_principal():
    titulo = 'Menu Principal'
    opcoes = {
        menu_pessoa()[0]: menu_pessoa,
        menu_funcionario()[0]: menu_funcionario,
        menu_cliente()[0]: menu_cliente
    }
    return [titulo, opcoes]
    
    
def menu_pessoa():
    titulo = 'Dados Pessoas'
    opcoes = {
        'Cadastrar Nova Pessoa': pessoas.cadastrar_pessoa,
        'Listar Pessoas Cadastradas': pessoas.listar_pessoas
    }
    return [titulo, opcoes]
    
    
def menu_funcionario():
    titulo = 'Dados Funcionários'
    opcoes = {
        'Cadastrar Novo Funcionário': funcionarios.cadastrar_funcionario,
        'Listar Funcionários Cadastrados': funcionarios.listar_funcionarios
    }
    return [titulo, opcoes]
    
    
def menu_cliente():
    titulo = 'Dados Cliente'
    opcoes = {
        'Cadastrar Nova Pessoa': clientes.cadastrar_cliente,
        'Listar Pessoas Cadastradas': clientes.listar_clientes
    }
    return [titulo, opcoes]
 
