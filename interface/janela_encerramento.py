import tkinter.messagebox
from tkinter import *
from funcoes import atualizar
from funcoes import encerrar
from interface import menu_superior as ms


def janelaEncerrar(root):
    def aviso():
        notice = tkinter.messagebox.askyesno("Confirmar", f"Deseja confirmar o "
                                                  f"encerramento de: "
                                                  f"{vinvestimento.get()}")
        print(notice) # >>>>>> APAGAR PRINT
        if notice:
                encerra = encerrar.Encerrar(vinvestimento.get())
                encerra.encerrarInvest()
                refresh_painel = ms.CriarMenuSuperior(root, encerrar_invest)
                refresh_painel.encerrar()


    encerrar_invest = Frame(root, borderwidth='1', relief='solid',
                        background="light "
                                                                      "gray")
    encerrar_invest.place(x=10, y=10, width=453, height=200)

    ms.CriarMenuSuperior(root, encerrar_invest)

    #Cadastro
    Label(encerrar_invest, text='Investimentos:', background="light gray",
          foreground='#009',
          anchor=W).place(x=20, y=10, width=100, height=20)
    try:
        investimentos = atualizar.consultaNome() #retorna uma lista com todos os
        # investimentos cadastrados
    except:
        Label(encerrar_invest, text='Não há investimentos cadastrados',
              background="red",
              foreground='white',
              anchor=W).place(x=70, y=60, width=190, height=20)
    else:
        if len(investimentos)>0:
            vinvestimento = StringVar()
            vinvestimento.set(investimentos[0])
            op_tipo = OptionMenu(encerrar_invest, vinvestimento,
                                 *investimentos)
            #
            # Foi
            # usado um * para
            # utilizar todos os valores da lista
            op_tipo.place(x=20, y=30, width=270, height=30)

            btn = Button(encerrar_invest, text="Encerrar", command=aviso)
            btn.place(x=20, y=140, width=70, height=20)
        else:
            Label(encerrar_invest, text='Não há investimentos cadastrados',
                  background="red",
                  foreground='white',
                  anchor=W).place(x=70, y=60, width=190, height=20)

def janelaDeEncerrados(root):
    """Frame para mostrar os investimentos que foram encerrados"""

    def semComando():
        print()

    encerrados_invest = Frame(root, borderwidth='1', relief='solid',
                        background="light "
                                                                      "gray")
    encerrados_invest.place(x=10, y=10, width=453, height=200)

    ms.CriarMenuSuperior(root, encerrados_invest)

    #Encerrados
    Label(encerrados_invest, text='Investimentos:', background="light gray",
          foreground='#009',
          anchor=W).place(x=20, y=10, width=100, height=20)

    botao_mostrar = Button(encerrados_invest, text="Mostrar",command=semComando)
    botao_mostrar.place(x=310, y=30, width=50, height=30)
    try:
        investimentos = encerrar.investsEncerrados() #retorna uma lista com todos os
        # investimentos cadastrados
    except:
        Label(encerrados_invest, text='Não há investimentos cadastrados',
              background="red",
              foreground='white',
              anchor=W).place(x=70, y=60, width=190, height=20)
    else:
        if len(investimentos)>0:
            vinvestimento = StringVar()
            vinvestimento.set(investimentos[0])
            op_tipo = OptionMenu(encerrados_invest, vinvestimento,
                                 *investimentos)
            #
            # Foi
            # usado um * para
            # utilizar todos os valores da lista
            op_tipo.place(x=20, y=30, width=270, height=30)
        else:
            Label(encerrados_invest, text='Não há investimentos cadastrados',
                  background="red",
                  foreground='white',
                  anchor=W).place(x=70, y=60, width=190, height=20)