import customtkinter as ctk
import textos as txt

#  Criação da interface:
win_width, win_height = 800, 600
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme('dark-blue')

def inicio():    
    janelaINICIAL = ctk.CTk() # criar janelaINICIAL
    # CONFIGURAÇÕES:
    janelaINICIAL.iconbitmap("imagem\logo.ico") # coloca logo no título da página
    janelaINICIAL.title("BIBLIOTECA LEsquivel05 | HOME") # título da página
    janelaINICIAL.geometry('{}x{}'.format(win_width, win_height)) # coloca um tamanho fixo da tela
    janelaINICIAL.resizable(False, False) # bloqueia o tamanho da tela

    # TEXTOS:
    ctk.CTkLabel(janelaINICIAL, text="\n\nSEJA BEM-VINDO(A)(E) A BIBLIOTECA LEsquivel05", font=("Montserrat", 20)).pack() # titulo
    ctk.CTkLabel(janelaINICIAL, text="\n\n\n\nPara qual parte deseja ir hoje?", font=("Montserrat", 18)).pack() # sub-titulo
    ctk.CTkButton(janelaINICIAL, command = publica, width=200, height=100, border_width=1, border_color='white', border_spacing=1, bg_color='red', text="PÚBLICA", font=("Montserrat", 30)).place(x=100, y = 300) # botão pública
    ctk.CTkButton(janelaINICIAL, command=privada, width=200, height=100, border_width=1, border_color='white', border_spacing=1, bg_color='red', text="PRIVADA", font=("Montserrat", 30)).place(x=400, y = 300) # botão privada

    janelaINICIAL.mainloop() # deixa janelaINICIAL ativa

def publica():
    janelaPUBLICA = ctk.CTkToplevel() # criar janelaPUBLICA

    # CONFIGURAÇÕES:
    janelaPUBLICA.iconbitmap("imagem\logo.ico") # coloca logo no título da página
    janelaPUBLICA.title("BIBLIOTECA LEsquivel05 | PÚBLICA") # título da página
    janelaPUBLICA.geometry('{}x{}'.format(win_width, win_height)) # coloca um tamanho fixo da tela
    janelaPUBLICA.resizable(False, False) # bloqueia o tamanho da tela

    # TEXTOS: 
    ctk.CTkLabel(janelaPUBLICA, text="\n\nBIBLIOTECA LEsquivel05: ACESSO PÚBLICO", font=("Montserrat", 20)).pack() # titulo
    ctk.CTkLabel(janelaPUBLICA, text="\n\n\n\nEssa é a nossa parte pública, o que deseja verificar?", font=("Montserrat", 18)).pack() # sub-titulo
    ctk.CTkButton(janelaPUBLICA, command=verACERVO, width=150, height=70, border_width=1, border_color='white', border_spacing=1, bg_color='red', text="VER ACERVO \n PÚBLICO", font=("Montserrat", 30)).place(x=50, y = 300) # botão ver acervo público
    ctk.CTkButton(janelaPUBLICA, command=sobre, width=150, height=70, border_width=1, border_color='white', border_spacing=1, bg_color='red', text="VER SOBRE", font=("Montserrat", 30)).place(x=300, y = 300) # botão ver sobre
    ctk.CTkButton(janelaPUBLICA, command=inicio, width=150, height=70, border_width=1, border_color='white', border_spacing=1, bg_color='red', text="IR PARA HOME", font=("Montserrat", 30)).place(x=500, y = 300) # botão voltar pro começo

    janelaPUBLICA.mainloop() # deixa janelaPUBLICA ativa
    
def sobre():
    janelaSOBRE = ctk.CTkToplevel() # criar janelaSOBRE

    # CONFIGURAÇÕES:
    janelaSOBRE.iconbitmap("imagem\logo.ico") # coloca logo no título da página
    janelaSOBRE.title("BIBLIOTECA LEsquivel05 | SOBRE") # título da página
    janelaSOBRE.geometry('{}x{}'.format(win_width, win_height)) # coloca um tamanho fixo da tela
    janelaSOBRE.resizable(False, False) # bloqueia o tamanho da tela

    # TEXTOS: 
    ctk.CTkLabel(janelaSOBRE, text="\n\nBIBLIOTECA LEsquivel05: SOBRE", font=("Montserrat", 20)).pack() # titulo
    ctk.CTkLabel(janelaSOBRE, text="\n\n\n\nConheça um pouco mais sobre a biblioteca LEsquivel05.", font=("Montserrat", 18)).pack() # sub-titulo
    ctk.CTkLabel(janelaSOBRE, wraplength=win_width, text=f"\n\n\n\n{txt.sobre}", width=200, height=100, font=("Montserrat", 15)).pack() # sub-titulo
    ctk.CTkButton(janelaSOBRE, command= inicio, width=100, height=50, border_width=1, border_color='white', border_spacing=1, bg_color='red', text="VOLTAR PRO INÍCIO", font=("Montserrat", 10)).place(x=10, y = 10) # botão voltar ao inicio

    janelaSOBRE.mainloop() # deixa janelaSOBRE ativa

def verACERVO():
    janelaACERVOVER = ctk.CTkToplevel() # criar janelaACERVOVER

    # CONFIGURAÇÕES:
    janelaACERVOVER.iconbitmap("imagem\logo.ico") # coloca logo no título da página
    janelaACERVOVER.title("BIBLIOTECA LEsquivel05 | PÚBLICA") # título da página
    janelaACERVOVER.geometry('{}x{}'.format(win_width, win_height)) # coloca um tamanho fixo da tela
    janelaACERVOVER.resizable(False, False) # bloqueia o tamanho da tela

    # TEXTOS: 
    ctk.CTkLabel(janelaACERVOVER, text="\n\nBIBLIOTECA LEsquivel05: ACERVO PÚBLICO", font=("Montserrat", 20)).pack() # titulo
    ctk.CTkLabel(janelaACERVOVER, text="\n\n\n\nEssa página ainda está sendo construída, favor tente mais tarde.", font=("Montserrat", 18)).pack() # sub-titulo
    ctk.CTkButton(janelaACERVOVER, command=inicio, width=100, height=50, border_width=1, border_color='white', border_spacing=1, bg_color='red', text="VOLTAR AO INÍCIO", font=("Montserrat", 15)).place(x=350, y = 200) # botão ver acervo público
    
    janelaACERVOVER.mainloop() # deixa janelaACERVOVER ativa

def privada():
    janelaPRIVADA = ctk.CTkToplevel() # criar janelaPRIVADA

    # CONFIGURAÇÕES:
    janelaPRIVADA.iconbitmap("imagem\logo.ico") # coloca logo no título da página
    janelaPRIVADA.title("BIBLIOTECA LEsquivel05 | ACESSAR") # título da página
    janelaPRIVADA.geometry('{}x{}'.format(win_width, win_height)) # coloca um tamanho fixo da tela
    janelaPRIVADA.resizable(False, False) # bloqueia o tamanho da tela

    # TEXTOS: 
    ctk.CTkLabel(janelaPRIVADA, text="\n\nBIBLIOTECA LEsquivel05: ACESSO RESTRITO", font=("Montserrat", 20)).pack() # titulo
    ctk.CTkLabel(janelaPRIVADA, text="\n\n\n\nPedimos que nos diga se deseja se CADASTRAR ou FAZER LOGIN", font=("Montserrat", 18)).pack() # sub-titulo
    ctk.CTkButton(janelaPRIVADA, command=cadastro, width=200, height=100, border_width=1, border_color='white', border_spacing=1, bg_color='red', text="CRIAR CADASTRO", font=("Montserrat", 30)).place(x=100, y = 300) # botão fazer cadastro
    ctk.CTkButton(janelaPRIVADA, command=login, width=200, height=100, border_width=1, border_color='white', border_spacing=1, bg_color='red', text="FAZER LOGIN", font=("Montserrat", 30)).place(x=400, y = 300) # botão fazer login

    janelaPRIVADA.mainloop() # deixa janelaPRIVADA ativa

def login():
    janelaLOGIN = ctk.CTkToplevel() # criar janelaLOGIN

    # CONFIGURAÇÕES:
    janelaLOGIN.iconbitmap("imagem\logo.ico") # coloca logo no título da página
    janelaLOGIN.title("BIBLIOTECA LEsquivel05 | LOGIN") # título da página
    janelaLOGIN.geometry('{}x{}'.format(win_width, win_height)) # coloca um tamanho fixo da tela
    janelaLOGIN.resizable(False, False) # bloqueia o tamanho da tela

    # TEXTOS: 
    ctk.CTkLabel(janelaLOGIN, text="\nBIBLIOTECA LEsquivel05: FAZER LOGIN.", font=("Montserrat", 20)).pack() # titulo
    ctk.CTkLabel(janelaLOGIN, text="\n\nEnte em nossa plataforma:", font=("Montserrat", 18)).pack() # sub-titulo
    ctk.CTkEntry(janelaLOGIN, placeholder_text="Coloque aqui o seu login.", width=300, height= 10).place(x=100, y=200)# login
    ctk.CTkEntry(janelaLOGIN, placeholder_text="Coloque aqui sua senha.", show="*", width=300, height= 10).place(x=100, y=240)# senha
    ctk.CTkCheckBox(janelaLOGIN, text="Lembrar-se de mim sempre").place(x=100, y=280)# lembrar-se de mim.
    ctk.CTkButton(janelaLOGIN, width=100, height=50, border_width=1, border_color='white', border_spacing=1, bg_color='red', text="ENTRAR", font=("Montserrat", 30)).place(x=170, y = 330) # botão entrar
    ctk.CTkButton(janelaLOGIN, width=50, height=30, border_width=1, border_color='blue', border_spacing=1, bg_color='red', text="ESQUECI MINHA SENHA", font=("Montserrat", 12)).place(x=250, y = 280) # botão esqueci minha senha
    ctk.CTkLabel(janelaLOGIN, text="Caso não tenha conta, cadastre-se:", font=("Montserrat", 12)).place(x=580, y = 370)# informa caso não tenha conta
    ctk.CTkButton(janelaLOGIN, command=cadastro, width=80, height=30, border_width=1, border_color='white', border_spacing=1, bg_color='red', text="FAZER CADASTRO", font=("Montserrat", 18)).place(x=580, y = 400) # botão cadastrar-se

    janelaLOGIN.mainloop() # deixa janelaLOGIN ativa
    
def cadastro():
    janelaCADASTRO = ctk.CTkToplevel() # criar janelaCADASTRO

    # CONFIGURAÇÕES:
    janelaCADASTRO.iconbitmap("imagem\logo.ico") # coloca logo no título da página
    janelaCADASTRO.title("BIBLIOTECA LEsquivel05 | CADASTRO") # título da página
    janelaCADASTRO.geometry('{}x{}'.format(win_width, win_height)) # coloca um tamanho fixo da tela
    janelaCADASTRO.resizable(False, False) # bloqueia o tamanho da tela

    # TEXTOS: 
    ctk.CTkLabel(janelaCADASTRO, text="\nBIBLIOTECA LEsquivel05: CADASTRAR-SE.", font=("Montserrat", 20)).pack() # titulo
    ctk.CTkLabel(janelaCADASTRO, text="\n\nCadastre-se em nossa plataforma:", font=("Montserrat", 18)).pack() # sub-titulo
    ctk.CTkEntry(janelaCADASTRO, placeholder_text="Coloque aqui o seu nome (completo ou social).", width=535, height= 10).place(x=40, y=200)# nome
    ctk.CTkEntry(janelaCADASTRO, placeholder_text="Coloque aqui sua idade.", show="*", width=535, height= 10).place(x=40, y=240)# idade
    ctk.CTkEntry(janelaCADASTRO, placeholder_text="Coloque aqui o seu sexo (M para MASCULINO, F para FEMININO e N para NÃO BINÁRIO).", width=535, height= 10).place(x=40, y=280)# sexo
    ctk.CTkEntry(janelaCADASTRO, placeholder_text="Coloque aqui seu telefone para contato (inclua o DDD).", show="*", width=535, height= 10).place(x=40, y=320)# telefone
    ctk.CTkEntry(janelaCADASTRO, placeholder_text="Coloque aqui seu documento.", show="*", width=535, height= 10).place(x=40, y=360)# documento
    ctk.CTkButton(janelaCADASTRO, width=100, height=50, border_width=1, border_color='white', border_spacing=1, bg_color='red', text="CADASTRAR", font=("Montserrat", 30)).place(x=170, y = 400) # botão cadastrar
    ctk.CTkLabel(janelaCADASTRO, text="Caso já tenha conta, entre:", font=("Montserrat", 12)).place(x=580, y = 420)# informa caso já tenha conta
    ctk.CTkButton(janelaCADASTRO, command=login, width=80, height=30, border_width=1, border_color='white', border_spacing=1, bg_color='red', text="FAZER LOGIN", font=("Montserrat", 18)).place(x=582, y = 442) # botão entrar

    janelaCADASTRO.mainloop() # deixa janelaCADASTRO ativa