from tkinter import *
from interface import painel_anual as pa, janela_atualizar, janela_adicionar, janela_encerramento


class CriarMenuSuperior():
    def __init__(self,root, destroyFrame):
        self.root = root
        self.destroyFrame = destroyFrame


    #Funções do Menu
    def semComando(self):
        print('')

    def cadastrar(self):
        self.destroyFrame.destroy()
        janela_adicionar.adicionarJanela(self.root)

    def atualizar(self):
        self.destroyFrame.destroy()
        janela_atualizar.janelaAtualizar(self.root)

    def encerrar(self):
        self.destroyFrame.destroy()
        janela_encerramento.janelaEncerrar(self.root)

    def mostrarEncerrados(self):
        self.destroyFrame.destroy()
        janela_encerramento.janelaDeEncerrados(self.root)

    def home(self):
        self.destroyFrame.destroy()
        pa.painelAnual(self.root)

    def criarBarraMenu(self):
        barraMenu = Menu(self.root)

        # Menu página inicial
        menuHome = Menu(barraMenu, tearoff=0)
        menuHome.add_command(label='Página Inicial',
                                  command=self.home)
        barraMenu.add_cascade(label='Home', menu=menuHome)


        #Menu atualizar
        menuAtualizar = Menu(barraMenu, tearoff=0)
        menuAtualizar.add_command(label='Atualizar investimentos',
                                      command=self.atualizar)
        barraMenu.add_cascade(label='Atualizar', menu=menuAtualizar)

        #Menu Criar
        menuCriar = Menu(barraMenu, tearoff=0)

        menuCriar.add_command(label='Adicionar novo investimento',
                                            command=self.cadastrar)
        barraMenu.add_cascade(label='Criar', menu=menuCriar)

        #Menu encerrar
        menuEncerrar = Menu(barraMenu, tearoff=0)
        menuEncerrar.add_command(label='Encerrar investimento', command=self.encerrar)
        menuEncerrar.add_separator()
        menuEncerrar.add_command(label='Visualizar encerrados', command=self.mostrarEncerrados)
        barraMenu.add_cascade(label='Encerrados', menu=menuEncerrar)


        #Menu relatório
        menuRelatorio = Menu(barraMenu, tearoff=0)
        menuRelatorio.add_command(label='Visualizar relatório anual', command=self.semComando)
        barraMenu.add_cascade(label='Relatório', menu=menuRelatorio)

        #Menu sobre
        menuSobre = Menu(barraMenu, tearoff=0)
        menuSobre.add_command(label='Redes Sociais', command=self.semComando)#futuramente
        # colocar um desvio para minhas redes sociais
        barraMenu.add_cascade(label='Sobre', menu=menuSobre)

        self.root.config(menu=barraMenu)