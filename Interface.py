# 1 - CRIAR UMA INTERFACE PYTHON
from tkinter import *

class Application:
    def __init__(self, master=None):
        # Adicione widgets e lógica aqui
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg =  Label(self.widget1, text = " Primeiro widget")
        self.msg.pack()

        #BUTTONS
        #Botão sair
        self.sair = Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["font"] = "Calibri", "10"
        self.sair["width"] = 10
        self.sair["command"] = self.widget1.quit
        self.sair.pack(side=RIGHT)

        #Botão Salvar
        self.salvar = Button(self.widget1)
        self.salvar["text"] = "Salvar"
        self.salvar["font"] = "Calibri", "10"
        self.salvar["width"] = 10
        self.salvar["command"] = self.widget1.quit
        self.salvar.pack(side=RIGHT)



        #Botão adicionar
        self.adicionar = Button(self.widget1)
        self.adicionar["text"] = "Adicionar"
        self.adicionar["font"] = "Calibri", "10"
        self.adicionar["width"] = 10
        self.adicionar["command"] = self.widget1.quit
        self.adicionar.pack(side=RIGHT)

        #EVENTOS
        # Ação Sair
        def mudarTexto(self):
            if self.msg["text"] == "Primeiro widget":
                self.msg["text"] = "O botão recebeu um clique"
            else:
                self.msg["text"] = "Primeiro widget"

root = Tk()
app = Application(root)
root.mainloop()
