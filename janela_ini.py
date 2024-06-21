from tkinter import *
from datetime import *
from interface import rodape as rdp, painel_anual as pa
from funcoes import cadastro

root = str(datetime.today())[:4]
root = Tk()
cadastro.criartabinvests()
root.title("Invest - Tela Inicial")
root.geometry("480x480")
root.resizable(False, False)
root.configure(background="light gray")

#Painel anual
pa.painelAnual(root)


rdp.CriarRodape(root)
