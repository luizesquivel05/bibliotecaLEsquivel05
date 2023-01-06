# página criada com o objetivo de realizar login e senha na aplicação.

# LEITURA DOS LOGINS DE CLIENTES
def lerCL():
    arqCL = 'administrativa\logCLIENTES.csv'
    logCL = open(arqCL)
    dadoslogCL = logCL.readlines()
    return dadoslogCL

# LEITURA DOS LOGINS DE CONTRIBUINTES
def lerCO():
    arqCO = 'administrativa\logCONTRIBUINTES.csv'
    logCO = open(arqCO)
    dadoslogCO = logCO.readlines()
    return dadoslogCO

# MANIPULAR LOGIN E SENHA
dadoCO = lerCO()
listaLOGINCO = list()
listaSENHACO = list()
for i in dadoCO:
    aux = i.split(';')
    listaLOGINCO.append(aux[0])
    listaSENHACO.append(aux[1])
dadoCL = lerCL()
listaLOGINCL = list()
listaSENHACL = list()
for i in dadoCL:
    aux = i.split(';')
    listaLOGINCL.append(aux[0])
    listaSENHACL.append(aux[1])

def tentarentrarCL(tentativalogin, tentativasenha):
    sucesso = str()
    if tentativalogin in listaLOGINCL and tentativasenha in listaSENHACL:
        if listaLOGINCL.index(tentativalogin) == listaSENHACL.index(tentativasenha):
            print('Logado como cliente')
            sucesso = "Sim"
        else:
            print('Favor verificar login e senha.')
            sucesso = "Não"
    else:
        print('Favor verificar login e senha.')
        sucesso = "Não"
    return sucesso

def tentarentrarCO(tentativalogin, tentativasenha):
    if tentativalogin in listaLOGINCO and tentativasenha in listaSENHACO:
        if listaLOGINCO.index(tentativalogin) == listaSENHACO.index(tentativasenha):
            print('Logado como contribuinte')
            sucesso = "Sim"
        else:
            print('Favor verificar login e senha.')
            sucesso = "Não"
    else:
        print('Favor verificar login e senha.')
        sucesso = "Não"
    return sucesso