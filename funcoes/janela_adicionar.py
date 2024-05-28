from tkinter import *
from funcoes import cadastro
from datetime import *
from funcoes import menu_superior as ms






def adicionarJanela(root):
    """Criar frame de adicionar investimentos dentro da tela principal"""

    def salvar():
        """Função para salvar o investimento no banco de dados"""
        salvar = cadastro.Cadastro(cinstitu.get(), vtipo.get(), vindexador.get(),
                                   ctaxa.get(), cdatini.get(), cdatres.get(),
                                   cvalor.get(), cin.get(), ccustodia.get())
        salvar.inseririnvest()
        salvar.criartab()
        refresh_painel = ms.CriarMenuSuperior(root, adicionar_invest)
        refresh_painel.cadastrar()

    ano = str(datetime.today())[:4]

    adicionar_invest = Frame(root, borderwidth='1', relief='solid',background="light gray")
    adicionar_invest.place(x=10, y=10, width=455, height=200)

    ms.CriarMenuSuperior(root, adicionar_invest)

    #Cadastro
    Label(adicionar_invest, text='Tipo:', background="light gray", foreground='#009',
          anchor=W).place(x=20, y=10, width=100, height=20)

    tipos = ["CDB", "LCI", "LCA", "Tesouro","Debênture"]

    vtipo = StringVar()
    vtipo.set(tipos[0])
    op_tipo = OptionMenu(adicionar_invest, vtipo, *tipos)  # Foi usado um * para
    # utilizar todos os valores da lista
    op_tipo.place(x=20, y=30, width=90, height=30)


    Label(adicionar_invest, text='Indexador:', background="light gray", foreground='#009',
          anchor=W).place(x=20, y=60, width=100, height=20)
    indexador = ["CDI", "SELIC", "IPCA", "Prefixado"]

    vindexador = StringVar()
    vindexador.set(indexador[0])
    op_indexador= OptionMenu(adicionar_invest, vindexador, *indexador)  # Foi usado um * para
    # utilizar todos os valores da lista
    op_indexador.place(x=20, y=80, width=90, height=30)


    Label(adicionar_invest, text='Banco/Instituição emissora:', background="light gray",
          foreground='#009',
          anchor=W).place(x=130, y=10, width=150, height=20)
    cinstitu = Entry(adicionar_invest) #entrada de texto
    cinstitu.place(x=130, y=30, width=200, height=20)

    Label(adicionar_invest, text='Taxa(%):', background="light gray",
          foreground='#009',
          anchor=W).place(x=130, y=60, width=100, height=20)
    ctaxa = Entry(adicionar_invest) #entrada de texto
    ctaxa.place(x=130, y=80, width=80, height=20)

    Label(adicionar_invest, text='Data de Início:', background="light gray",
          foreground='#009',
          anchor=W).place(x=340, y=10, width=80, height=20)
    cdatini = Entry(adicionar_invest) #entrada de texto
    cdatini.place(x=340, y=30, width=100, height=20)

    Label(adicionar_invest, text='Data de Resgate:', background="light gray",
          foreground='#009',
          anchor=W).place(x=340, y=60, width=90, height=20)
    cdatres = Entry(adicionar_invest) #entrada de texto
    cdatres.place(x=340, y=80, width=100, height=20)

    Label(adicionar_invest, text='IN:', background="light gray",
          foreground='#009',
          anchor=W).place(x=220, y=110, width=40, height=20)
    cin = Entry(adicionar_invest) #entrada de texto
    cin.place(x=220, y=130, width=40, height=20)

    Label(adicionar_invest, text='Valor:', background="light gray", foreground='#009',
          anchor=W).place(x=225, y=60, width=80, height=20)
    cvalor = Entry(adicionar_invest) #entrada de texto
    cvalor.place(x=225, y=80, width=100, height=20)

    Label(adicionar_invest, text='Instiruição com a custódia', background="light gray",
          foreground='#009',anchor=W).place(x=20, y=110, width=145, height=20)
    ccustodia = Entry(adicionar_invest) #entrada de texto
    ccustodia.place(x=20, y=130, width=180, height=20)


    btn = Button(adicionar_invest, text="Salvar", command=salvar)
    btn.place(x=370, y=160, width=70, height=20)
