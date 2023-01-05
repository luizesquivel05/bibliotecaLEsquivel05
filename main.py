from textos import *
import funcoes as fn
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
        else:
            os.system('cls')
            print(logarCL)
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