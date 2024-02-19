from tkinter import *
from funcoes import cadastro
import os
import subprocess
from datetime import *

def semComando():
    print('')

def cadastrar():
    subprocess.Popen(["python", "janela_adicionar.py"])

def salvar():
    salvar = cadastro.Cadastro(cinstitu.get(), vtipo.get(), vindexador.get(),ctaxa.get(),cdatini.get(),cdatres.get(),cvalor.get(),cin.get() )
    salvar.criartabinvests()
    salvar.inseririnvest()
    salvar.criartab()



ano = str(datetime.today())[:4]
app = Tk()

app.title("Invest - Tela Inicial")
app.geometry("345x250")
app.configure(background="light gray")


barraMenu = Menu(app)

#Menu atualizar
menuAtualizar = Menu(barraMenu, tearoff=0)
menuAtualizar.add_command(label='Atualizar investimentos',
                              command=semComando)
barraMenu.add_cascade(label='Atualizar', menu=menuAtualizar)

#Menu Criar
menuCriar = Menu(barraMenu, tearoff=0)

menuCriar.add_command(label='Adicionar novo investimento',
                                    command=cadastrar)
barraMenu.add_cascade(label='Criar', menu=menuCriar)

#Menu encerrar
menuEncerrar = Menu(barraMenu, tearoff=0)
menuEncerrar.add_command(label='Encerrar investimento', command=semComando)
menuEncerrar.add_separator()
menuEncerrar.add_command(label='Visualizar encerrados', command=semComando)
barraMenu.add_cascade(label='Encerrados', menu=menuEncerrar)


#Menu relatório
menuRelatorio = Menu(barraMenu, tearoff=0)
menuRelatorio.add_command(label='Visualizar relatório anual', command=semComando)
barraMenu.add_cascade(label='Relatório', menu=menuRelatorio)

#Menu sobre
menuSobre = Menu(barraMenu, tearoff=0)
menuSobre.add_command(label='Redes Sociais', command=semComando)#futuramente
# colocar um desvio para minhas redes sociais
barraMenu.add_cascade(label='Sobre', menu=menuSobre)

app.config(menu=barraMenu)

#Cadastro
Label(app, text='Tipo:', background="light gray", foreground='#009',
      anchor=W).place(x=20, y=10, width=100, height=20)

tipos = ["CDB", "LCI", "LCA", "Tesouro","Debênture"]

vtipo = StringVar()
vtipo.set(tipos[0])
op_tipo = OptionMenu(app, vtipo, *tipos)  # Foi usado um * para
# utilizar todos os valores da lista
op_tipo.place(x=20, y=30, width=90, height=30)


Label(app, text='Indexador:', background="light gray", foreground='#009',
      anchor=W).place(x=20, y=60, width=100, height=20)
indexador = ["CDI", "SELIC", "IPCA", "Prefixado"]

vindexador = StringVar()
vindexador.set(indexador[0])
op_indexador= OptionMenu(app, vindexador, *indexador)  # Foi usado um * para
# utilizar todos os valores da lista
op_indexador.place(x=20, y=80, width=90, height=30)


Label(app, text='Banco/Instituição:', background="light gray",
      foreground='#009',
      anchor=W).place(x=130, y=10, width=100, height=20)
cinstitu = Entry(app) #entrada de texto
cinstitu.place(x=130, y=30, width=200, height=20)

Label(app, text='Taxa(%):', background="light gray",
      foreground='#009',
      anchor=W).place(x=130, y=60, width=100, height=20)
ctaxa = Entry(app) #entrada de texto
ctaxa.place(x=130, y=80, width=80, height=20)

Label(app, text='Data de Início:', background="light gray",
      foreground='#009',
      anchor=W).place(x=230, y=60, width=120, height=20)
cdatini = Entry(app) #entrada de texto
cdatini.place(x=230, y=80, width=100, height=20)

Label(app, text='Data de Resgate:', background="light gray",
      foreground='#009',
      anchor=W).place(x=230, y=110, width=120, height=20)
cdatres = Entry(app) #entrada de texto
cdatres.place(x=230, y=130, width=100, height=20)

Label(app, text='IN:', background="light gray",
      foreground='#009',
      anchor=W).place(x=180, y=110, width=40, height=20)
cin = Entry(app) #entrada de texto
cin.place(x=180, y=130, width=40, height=20)

Label(app, text='Valor:', background="light gray", foreground='#009',
      anchor=W).place(x=20, y=110, width=100, height=20)
cvalor = Entry(app) #entrada de texto
cvalor.place(x=20, y=130, width=150, height=20)


btn = Button(app, text="Salvar", command=salvar)
btn.place(x=257, y=180, width=70, height=20)




##Rodapé
txt1 = Label(app, text='Criado por Marcos Erbas Jr', background="light gray",
             foreground="#000")
txt1.place(x=10, y=220, width=150, height=30)

txt1 = Label(app, text='Versão: 1.0.24', background="light gray",
             foreground="#000")
txt1.place(x=210, y=220, width=150, height=30)

app.mainloop()