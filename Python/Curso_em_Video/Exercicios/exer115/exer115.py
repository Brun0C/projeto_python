from menu import menus, menu
from uteis import limpar_tela

ir_para = menus.menu_principal
voltar_para = {}

while ir_para:
    limpar_tela()
    dados = ir_para() #se modulo for um menu, retorna uma tupla contendo titulo e opções, senão retorna None
    
    if dados:
        titulo, opcoes = dados #descompacta tupla contendo titulo e opções
        
        while ir_para in list(voltar_para.values()):
            voltar_para.popitem() #remove o valor de 'voltar_para' até que 'ir_para' não esteja contido nele

        opcoes.update(voltar_para) #adiciona os valores de 'voltar_para' para serem exibidos no menu
        voltar_para[f'Voltar ao {titulo}'] = ir_para #caminho percorrido entre menus
	    
        ir_para = menu.exibir_menu(titulo, opcoes) #cria o menu e retorna o caminho do modulo seguinte
        
    else:
        _, ir_para = voltar_para.popitem()
        
print('\nFinalizando o Programa...')
