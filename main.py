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
            lg.tentarentrarCO(login, senha)
        else:
            os.system('cls')
            print(logarCL)
            login = str(input('Digite o login: '))
            senha = str(input('Digite o senha: '))
            lg.tentarentrarCL(login, senha)
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
                    else: break
                informacoes = str()
                informacoes += nome + ";"
                informacoes += idade + ";"
                informacoes += sexo + ";"
                informacoes += telefone + ";"
                informacoes += documento
                atualizacao = open('administrativa\dadosCLIENTES.csv', 'a+')
                atualizacao.write(informacoes)
                atualizacao.write('\n')
else:
    os.system('cls')
    print(sobre)
    print('''
        Deseja encerrar o programa? 0 para ENCERRAR O PROGRAMA ou 1 para VOLTAR AO INÍCIO.      
    ''')
    verificacao = int(input())
    if verificacao == 1:
        os.system('cls')
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
                    lg.tentarentrarCO(login, senha)
                else:
                    os.system('cls')
                    print(logarCL)
                    login = str(input('Digite o login: '))
                    senha = str(input('Digite o senha: '))
                    lg.tentarentrarCL(login, senha)
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
                            else: break
                        informacoes = str()
                        informacoes += nome + ";"
                        informacoes += idade + ";"
                        informacoes += sexo + ";"
                        informacoes += telefone + ";"
                        informacoes += documento
                        atualizacao = open('administrativa\dadosCLIENTES.csv', 'a+')
                        atualizacao.write(informacoes)
                        atualizacao.write('\n')
    else: i = 0