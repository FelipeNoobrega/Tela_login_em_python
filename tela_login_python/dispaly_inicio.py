from cProfile import label
from tkinter import *
import codigo as co
import cadastros as c
import display as d
import time



def tela_inicial():
    d.pg_cadastros.destroy()
    time.sleep(0.3)

    pg_inicio = Tk()
    pg_inicio.title("INICIO")
    pg_inicio.geometry("490x560+610+153")
    pg_inicio.iconbitmap(default="")
    pg_inicio.resizable(width=0, height=1)

    #variaveis
    img_fundo_inicio = PhotoImage(file="images\\inicio_fundo.png")
    img_config = PhotoImage(file="images\\btn_config.png")
    

    #lables
    lab_fundo = Label(pg_inicio, bg="black",image=img_fundo_inicio)
    lab_fundo.pack()
    label_alert = Label(pg_inicio, bg="grey", text="",font=("Calibri", 10), justify=CENTER)
    

    #caixa de entrada
    entra_nome = Entry(pg_inicio,bd=2, font=("Calibri", 20), justify=CENTER)
    entra_nome.place(width=285, height=42, x=154, y=123)

    entra_idade = Entry(pg_inicio,bd=2, font=("Calibri", 20), justify=CENTER)
    entra_idade.place(width=285, height=42, x=154, y=214)

    
    
    # botão
    btn_configura = Button(pg_inicio,bg="black", bd=2, image=img_config, command=configuracao )
    btn_configura.place(width=131, height=72, x=179, y=464)

    def configuracao():

        #botões de da aba de configurações 
        btn_cadastro=Button(pg_inicio,bg="black", bd=2, image=img_enviar_cadastro, command=cadastrar )
        btn_cadastro.place(width=131, height=72, x=179, y=464)

        btn_cadastro=Button(pg_inicio,bg="black", bd=2, image=img_enviar_cadastro, command=cadastrar )
        btn_cadastro.place(width=131, height=72, x=179, y=464)

        btn_cadastro=Button(pg_inicio,bg="black", bd=2, image=img_enviar_cadastro, command=cadastrar )
        btn_cadastro.place(width=131, height=72, x=179, y=464)
    

    pg_inicio.mainloop()

