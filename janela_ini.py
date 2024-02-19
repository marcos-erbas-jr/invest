from tkinter import *
import os
import subprocess
from datetime import *

def semComando():
    print('')

def cadastrar():
    subprocess.Popen(["python", "janela_adicionar.py"])

ano = str(datetime.today())[:4]
app = Tk()

app.title("Invest - Tela Inicial")
app.geometry("480x480")
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



##Parte da tabela anual
invest_anual = Frame(app,borderwidth=1, relief="solid")
invest_anual.place(x=10, y=10, width=455, height=419)

listaFiltro = ["2023", "2024", "2025", "2026","2027"]

vfiltro = StringVar()
vfiltro.set(ano)
bl_filtro = Label(invest_anual, text="Investimentos de:",
                  background="light blue",font=("Helvetica",17, "bold") )
bl_filtro.place(x=0, y=0, width=453, height=30)
op_filtro = OptionMenu(invest_anual, vfiltro, *listaFiltro)  # Foi usado um * para
# utilizar todos os valores da lista
op_filtro.place(x=350, y=0, width=80, height=30)

#Título da tabela anual
mes = Label(invest_anual,text="Mês",borderwidth=1, relief="solid",
                     background="light green")
mes.place(x=5, y=30, width=110, height=30)
valor = Label(invest_anual,text="Valor",borderwidth=1, relief="solid",
                     background="light green")
valor.place(x=116, y=30, width=110, height=30)
rend = Label(invest_anual,text="Rendimento",borderwidth=1, relief="solid",
                     background="light green")
rend.place(x=227, y=30, width=110, height=30)
taxa = Label(invest_anual,text="Taxa",borderwidth=1, relief="solid",
                     background="light green")
taxa.place(x=338, y=30, width=110, height=30)

#tabela

meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Aug", "Set",
         "Nov", "Dez"]
pos_y = 61

for elementos in meses:
    mes_name = Label(invest_anual, text=f"{elementos}", borderwidth=1, relief="solid",
                    background="white")
    mes_name.place(x=5, y=pos_y, width=110, height=30)
    valor_mes = Label(invest_anual, text="R$xxxx", borderwidth=1,
                      relief="solid",
                      background="white")
    valor_mes.place(x=116, y=pos_y, width=110, height=30)
    rend_mes = Label(invest_anual, text="R$xx", borderwidth=1, relief="solid",
                     background="white")
    rend_mes.place(x=227, y=pos_y, width=110, height=30)
    taxa_mes = Label(invest_anual, text="x%", borderwidth=1, relief="solid",
                     background="white")
    taxa_mes.place(x=338, y=pos_y, width=110, height=30)
    pos_y += 32


##Rodapé
txt1 = Label(app, text='Criado por Marcos Erbas Jr', background="light gray",
             foreground="#000")
txt1.place(x=10, y=450, width=150, height=30)

txt1 = Label(app, text='Versão: 1.0.24', background="light gray",
             foreground="#000")
txt1.place(x=350, y=450, width=150, height=30)

app.mainloop()