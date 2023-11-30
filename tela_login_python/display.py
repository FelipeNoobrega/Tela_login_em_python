'''from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)
root.mainloop()'''

'''import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

root = tk.Tk()
myapp = App(root)
myapp.mainloop()'''


from cProfile import label
from tkinter import *
import codigo as co
import cadastros as c
import dispaly_inicio as dis
import time


# funções de interação da janela 

def valida():
    entra = entradaToken.get()
    senha = entradaSenha.get()
    testa = c.entrar(entra,senha)
    print(testa)
    if testa[0]!=False:
        lab_mensagem["text"]="Cadastro não encontrado"
        
    else:
        lab_mensagem["text"]="Sucesso"

def janelaCadastros():
    pagina.destroy()
    time.sleep(0.3)

    pg_cadastros=Tk()
    pg_cadastros.title("cadastros")
    pg_cadastros.geometry("490x560+610+153")
    pg_cadastros.iconbitmap(default="")
    pg_cadastros.resizable(width=0, height=1)

    #funções janela cadastros
    def cadastrar():
        nome = entra_nome.get()
        idade = int(entra_idade.get())
        senha = entra_senha.get()
        conf = confirma_senha.get()
        if senha == conf:
            conf = co.codifica(senha)
            c.insereCadastro(nome,idade,senha,conf)
            label_alert["text"]="sucesso!!!"
            label_alert.place(width=140, height=22, x=10, y=522)
            time.sleep(0.3)
            dis.tela_inicial()
        
        else:
            label_alert["text"]="senhas estão distintas!"
            label_alert.place(width=140, height=22, x=10, y=522)


    #variaveis
    img_fundo_cadastro = PhotoImage(file="images\\Cadastro_fundo.png")
    img_enviar_cadastro = PhotoImage(file="images\\btn_enviar.png")
    esconda_senha = StringVar()
    confirma_senha = StringVar()

    #lables
    lab_fundo = Label(pg_cadastros, bg="black",image=img_fundo_cadastro)
    lab_fundo.pack()
    label_alert = Label(pg_cadastros, bg="grey", text="",font=("Calibri", 10), justify=CENTER)
    

    #caixa de entrada
    entra_nome = Entry(pg_cadastros,bd=2, font=("Calibri", 20), justify=CENTER)
    entra_nome.place(width=285, height=42, x=154, y=123)

    entra_idade = Entry(pg_cadastros,bd=2, font=("Calibri", 20), justify=CENTER)
    entra_idade.place(width=285, height=42, x=154, y=214)

    entra_senha = Entry(pg_cadastros,bd=2, textvariable=esconda_senha, show="*",font=("Calibri", 20), justify=CENTER)
    entra_senha.place(width=285, height=42, x=155, y=304)

    entra_confirma = Entry(pg_cadastros,bd=2, textvariable=confirma_senha, show="*", font=("Calibri", 20), justify=CENTER)
    entra_confirma.place(width=285, height=42, x=155, y=395)
    
    # botão
    btn_cadastro=Button(pg_cadastros,bg="black", bd=2, image=img_enviar_cadastro, command=cadastrar )
    btn_cadastro.place(width=131, height=72, x=179, y=464)

    

    pg_cadastros.mainloop()

#janela login
pagina=Tk()
pagina.title("Login")
pagina.geometry("490x560+610+153")
pagina.iconbitmap(default="")
pagina.resizable(width=0, height=1)

#variaveis globais
esconda_senha = StringVar()

#importar imagens 
img_fundo = PhotoImage(file="images\\fundo.png")
img_btn_cadastro = PhotoImage(file="images\\btn_cadastro.png")
img_btn_login = PhotoImage(file="images\\btn_login.png")

#lables 
lab_fundo = Label(pagina, bg="black",image=img_fundo)
lab_fundo.pack()


# caixa de entrada 
entradaToken = Entry(pagina,bd=2, font=("Calibri", 20), justify=CENTER)
entradaToken.place(width=365, height=58, x=63, y=194)

entradaSenha = Entry(pagina,bd=2, textvariable=esconda_senha, show="*", font=("Calibri", 20), justify=CENTER)
entradaSenha.place(width=365, height=58, x=63, y=304)

lab_mensagem = Label(pagina,font=("Calibri", 20),bg="grey",)
lab_mensagem.place(x=63, y=498)

#botões
btn_entrar=Button(pagina,bg="black",bd=2, image=img_btn_login, command=valida)
btn_entrar.place(width=161, height=74, x=167, y=417)

btn_cadastro=Button(pagina,bg="black", bd=2, image=img_btn_cadastro, command=janelaCadastros )
btn_cadastro.place(width=162, height=43, x=319, y=96)

pagina.mainloop()