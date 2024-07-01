import tkinter.messagebox
from tkinter import *
from funcoes import atualizar
from funcoes import validacao_atualizacao
from datetime import *
from interface import menu_superior as ms
from informacoes import filtros_calendario as fc


def janelaAtualizar(root):
    def aviso():
        notice = tkinter.messagebox.askyesno("Confirmar", f"Deseja salvar a "
                                                  f"atualização: "
                                                  f"{vinvestimento.get()}\n"
                                                  f"{vmes.get()}/"
                                                  f"{vano.get()} R$"
                                                  f"{cvalor.get()}")
        print(notice) # >>>>>> APAGAR PRINT
        if notice:
                validar = validacao_atualizacao.Validar(vmes.get(), cvalor.get(),vinvestimento.get(), vano.get())
                validar = validar.validacao()
                print(validar)
                if validar == 1:
                    notice = tkinter.messagebox.showwarning("Erro", f"Não foi possível salvar esta atualização, "
                                                                    f"a data da atualização é anterior a data inicial.")
                if validar == 2:
                    notice = tkinter.messagebox.showwarning("Erro", f"Não foi possível salvar esta atualização, "
                                                                    f"a data da atualização é superior a data de resgate.")
                refresh_painel = ms.CriarMenuSuperior(root, atualizar_invest)
                refresh_painel.atualizar()


    atualizar_invest = Frame(root, borderwidth='1', relief='solid',background="light gray")
    atualizar_invest.place(x=10, y=10, width=453, height=200)

    ms.CriarMenuSuperior(root, atualizar_invest)

    #Cadastro
    Label(atualizar_invest, text='Investimentos:', background="light gray",
          foreground='#009',
          anchor=W).place(x=20, y=10, width=100, height=20)
    try:
        investimentos = atualizar.consultaNome() #retorna uma lista com todos os
        # investimentos cadastrados
    except:
        Label(atualizar_invest, text='Não há investimentos cadastrados',
              background="red",
              foreground='white',
              anchor=W).place(x=70, y=60, width=190, height=20)
    else:
        if len(investimentos)>0:
            vinvestimento = StringVar()
            vinvestimento.set(investimentos[0])
            op_tipo = OptionMenu(atualizar_invest, vinvestimento,
                                 *investimentos)
            #
            # Foi
            # usado um * para
            # utilizar todos os valores da lista
            op_tipo.place(x=20, y=30, width=270, height=30)

            Label(atualizar_invest, text='Mês:', background="light gray",
                  foreground='#009',
                  anchor=W).place(x=300, y=10, width=35, height=20)
            mes = fc.meses
            mes_atual = int(str(datetime.date(datetime.today()))[5:7])-1

            vmes = StringVar()
            vmes.set(mes[mes_atual])
            op_indexador= OptionMenu(atualizar_invest, vmes, *mes)  # Foi usado
            # um *
            # para
            # utilizar todos os valores da lista
            op_indexador.place(x=300, y=30, width=60, height=30)

            Label(atualizar_invest, text='Ano:', background="light gray",
                  foreground='#009',
                  anchor=W).place(x=370, y=10, width=30, height=20)
            ano = fc.anos
            ano_atual = str(datetime.date(datetime.today()))[:4]

            vano = StringVar()
            vano.set(ano[ano.index(ano_atual)])
            if vano == "Auto":
                vano = str(datetime.today().year)
            op_indexador = OptionMenu(atualizar_invest, vano, *ano)  # Foi
            # usado
            # um *
            # para
            # utilizar todos os valores da lista
            op_indexador.place(x=370, y=30, width=70, height=30)

            Label(atualizar_invest, text='Valor:', background="light gray",
                  foreground='#009',
                  anchor=W).place(x=20, y=70, width=100, height=20)
            cvalor = Entry(atualizar_invest) #entrada de texto
            cvalor.place(x=20, y=90, width=100, height=25)


            btn = Button(atualizar_invest, text="Salvar", command=aviso)
            btn.place(x=20, y=140, width=70, height=20)
        else:
            Label(atualizar_invest, text='Não há investimentos cadastrados',
                  background="red",
                  foreground='white',
                  anchor=W).place(x=70, y=60, width=190, height=20)