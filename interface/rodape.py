from tkinter import *
def CriarRodape(app):
    ##Rodapé
    txt1 = Label(app, text='Criado por Marcos Erbas Jr', background="light gray",
                 foreground="#000")
    txt1.place(x=10, y=450, width=150, height=30)

    txt1 = Label(app, text='Versão: 1.0.24', background="light gray",
                 foreground="#000")
    txt1.place(x=350, y=450, width=150, height=30)

    app.mainloop()