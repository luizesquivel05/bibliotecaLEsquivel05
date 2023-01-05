from textos import *
import funcoes as fn
import logar as lg
import os

print(inicio)
iniciar = int(input())
if fn.leituramenu(0, 1, iniciar) == 0:
    os.system('cls')
    print(verLOGIN)
    iniciar = int(input())
    if fn.leituramenu(0, 1, iniciar) == 0:
        os.system('cls')
        print(logar)
        iniciar = int(input())
        if fn.leituramenu(0, 1, iniciar) == 0:
            os.system('cls')
            print(logarCO)
            login = str(input())
            senha = str(input())
            lg.tentarentrarCO(login, senha)
        else:
            os.system('cls')
            print(logarCL)
            login = str(input())
            senha = str(input())
            lg.tentarentrarCL(login, senha)
    else:
        os.system('cls')
        print(cadastrar)
        iniciar = int(input())
        if fn.leituramenu(0, 1, iniciar) == 0:
            os.system('cls')
            print(cadastrarCO)
        else:
            os.system('cls')
            print(cadastrarCL)
else:
    os.system('cls')
    print(sobre)