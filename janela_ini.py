from tkinter import *
from datetime import *
from funcoes import rodape as rdp
from funcoes import cadastro
from funcoes import painel_anual as pa
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
