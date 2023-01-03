from textos import *
import os

while True:
    print(inicio)
    leitura = int(input())
    if leitura == 0:
        os.system('cls')
        print(verLOGIN)
        leitura = int(input())
        if leitura == 0:
            os.system('cls')
            print(logar)
            leitura = int(input())
            if leitura == 0:
                os.system('cls')
                print(logarCO)
            elif leitura == 1:
                os.system('cls')
                print(logarCL)
        elif leitura == 1:
            os.system('cls')
            print(cadastrar)
            leitura = int(input())
            if leitura == 0:
                os.system('cls')
                print(cadastrarCO)
            elif leitura == 1:
                os.system('cls')
                print(cadastrarCL)
    elif leitura == 1:
        os.system('cls')
        print(sobre)
    else:
        os.system('cls')
        break