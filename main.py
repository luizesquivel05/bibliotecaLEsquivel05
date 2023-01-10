from textos import *
import funcoes as fn
import logar as lg
import cadastrar as cd
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
            login = str(input('Digite o login: '))
            senha = str(input('Digite o senha: '))
            while lg.tentarentrarCO(login, senha) != "Sim":
                login = str(input('Digite o login: '))
                senha = str(input('Digite o senha: '))
            else:
                os.system('cls')
                print(loginCONTRIBUINTE)
                verificacao = int(input())
                if verificacao == 0: fn.menu()
                elif verificacao == 1: fn.acervo()
                elif verificacao == 2: print(sobre)
                elif verificacao == 3: 
                    print(atividadesADM)
                    verificacao = int(input())
                    if verificacao == 0: fn.menu()
                    elif verificacao == 1: fn.acervoADD()
                    elif verificacao == 3: fn.acervo()
        else:
            os.system('cls')
            print(logarCL)
            login = str(input('Digite o login: '))
            senha = str(input('Digite o senha: '))
            while lg.tentarentrarCL(login, senha) != "Sim":
                login = str(input('Digite o login: '))
                senha = str(input('Digite o senha: '))
            os.system('cls')
            print('''
                Deseja encerrar o programa? 0 para ENCERRAR O PROGRAMA ou 1 para VOLTAR AO INÍCIO.
            ''')
            verificacao = int(input())
            if verificacao == 1: fn.menu()
    else:
        os.system('cls')
        print(cadastrar)
        iniciar = int(input())
        if fn.leituramenu(0, 1, iniciar) == 0:
            os.system('cls')
            print(cadastrarCO)
            print('''
                Deseja encerrar o programa? 0 para ENCERRAR O PROGRAMA ou 1 para VOLTAR AO INÍCIO.
            ''')
            verificacao = int(input())
            if verificacao == 1: fn.menu()
        else:
            os.system('cls')
            print(cadastrarCL)
            if str(input()) == "S":
                #número de documento, sexo, nome e idade. 
                nome = str(input('Digite seu nome completo: '))
                idade = str(input('Digite sua idade: '))
                sexo = str(input('Digite seu sexo: (F para feminino, M para masculino e N para nenhum dos 2) '))
                telefone = str(input('Digite seu telefone: '))
                documento = str(input('Digite seu documento válido: '))
                while True:
                    if cd.validarCPF == 0:
                        documento = str(input('Digite seu CPF válido: '))
                        if cd.validarCPF == 0: continue
                        else: 
                            break
                    else: 
                        break
                informacoes = str()
                informacoes += nome + ";"
                informacoes += idade + ";"
                informacoes += sexo + ";"
                informacoes += telefone + ";"
                informacoes += documento
                atualizacao = open('administrativa\dadosCLIENTES.csv', 'a+')
                atualizacao.write(informacoes)
                atualizacao.write('\n')
                os.system('cls')
                print(cadastroCONCLUIDO)
                if int(input()) == 1: fn.menu()
else:
    os.system('cls')
    print(aberta)
    print('''
        Deseja encerrar o programa? 0 para ENCERRAR O PROGRAMA ou 1 para VOLTAR AO INÍCIO.
    ''')
    verificacao = int(input())
    if verificacao == 0:
        os.system('cls')
        fn.menu()
        print('''
            Deseja encerrar o programa? 0 para ENCERRAR O PROGRAMA ou 1 para VOLTAR AO INÍCIO.
        ''')
        verificacao = int(input())
        if verificacao == 1: fn.menu()
    elif verificacao == 1:
        os.system('cls')
        print(verACERVO)
        print('\n\n', fn.acervo())
        print('''
            Deseja encerrar o programa? 0 para ENCERRAR O PROGRAMA ou 1 para VOLTAR AO INÍCIO.
        ''')
        verificacao = int(input())
        if verificacao == 1: fn.menu()
        elif verificacao == 2:
            os.system('cls')
            print(sobre)
            print('''
                Deseja encerrar o programa? 0 para ENCERRAR O PROGRAMA ou 1 para VOLTAR AO INÍCIO.
            ''')
            verificacao = int(input())
        elif verificacao == 1: fn.menu()
        elif verificacao == 3: breakpoint