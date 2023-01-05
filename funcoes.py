# Nesse arquivo iremos colocar as funções usadas na aplicação

# função que gera leitura do menu.
def leituramenu(cond1, cond2, leitura):
    resultado = ""
    if leitura == 0: resultado = cond1
    elif leitura == cond2: resultado = cond2
    else:
        while True:
            if leitura == cond1 or leitura == cond2: 
                if leitura == cond1: 
                    resultado = cond1
                    break
                elif leitura == cond2: 
                    resultado = cond2
                    break
            else:
                leitura = int(input())
                if leitura == cond1 or leitura == cond2: 
                    if leitura == cond1: 
                        resultado = cond1
                        break
                    elif leitura == cond2: 
                        resultado = cond2
                        break
    return resultado