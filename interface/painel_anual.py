from tkinter import *
from interface import menu_superior as ms
from funcoes import mostrar_painel
from datetime import *

def painelAnual(root):
    filtro = datetime.date(datetime.today())
    ano = str(filtro)[:4]
    def mostrarPainel(filtro):
        meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Aug", "Set",
                 "Out",
                 "Nov", "Dez"]
        valores_painel = mostrar_painel.construir_painel(filtro)
        print(valores_painel)
        pos_y = 61

        for elementos in meses:
            n = meses.index(elementos)
            mes_name = Label(invest_anual, text=f"{elementos}", borderwidth=1,
                             relief="solid", background="white")
            mes_name.place(x=5, y=pos_y, width=110, height=30)
            valor_mes = Label(invest_anual, text=f"R$ {valores_painel[0][n]}",
                              borderwidth=1, relief="solid", background="white")
            valor_mes.place(x=116, y=pos_y, width=110, height=30)
            rend_mes = Label(invest_anual, text=f"R$ {valores_painel[1][n]}",
                             borderwidth=1, relief="solid", background="white")
            rend_mes.place(x=227, y=pos_y, width=110, height=30)
            taxa_mes = Label(invest_anual, text=f"{valores_painel[2][n]} %",
                             borderwidth=1, relief="solid", background="white")
            taxa_mes.place(x=338, y=pos_y, width=110, height=30)
            pos_y += 32
    invest_anual = Frame(root,borderwidth=1, relief="solid")
    invest_anual.place(x=10, y=5, width=455, height=445)

    barra_superior = ms.CriarMenuSuperior(root, invest_anual)
    barra_superior.criarBarraMenu()

    listaFiltro = ["2023", "2024", "2025", "2026","2027"]

    vfiltro = StringVar()
    vfiltro.set(listaFiltro[1])
    bl_filtro = Label(invest_anual, text="Investimentos de:",
                      background="light blue",font=("Helvetica",17, "bold"),
                      anchor="w" )
    bl_filtro.place(x=0, y=0, width=453, height=30)
    op_filtro = OptionMenu(invest_anual, vfiltro, *listaFiltro)
    # Foi usado um * para utilizar todos os valores da lista
    op_filtro.place(x=220, y=0, width=80, height=30)
    botao_mostrar = Button(invest_anual, text="Mostrar",
                           command=lambda:mostrarPainel(vfiltro.get()),
                           background="yellow")
    botao_mostrar.place(x=330, y=3, width=80, height=25)



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
    mostrarPainel(ano)



