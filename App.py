from conexoes_redes import Redes
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 200
        self.container2["pady"] = 3
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()
#-----
        self.titulo = Label(self.container1, text="Informe os dados:")
        self.titulo["font"] = ("Calibri", "15", "bold")
        self.titulo.pack()

        self.lb_id_redes = Label(self.container2, text="id:", font=self.fonte, width=10)
        self.lb_id_redes.pack(side=LEFT)

        self.txt_id_rede = Entry(self.container2)
        self.txt_id_rede["width"] = 10
        self.txt_id_rede["font"] = self.fonte
        self.txt_id_rede.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarRede
        self.btnBuscar.pack(side=RIGHT)

        self.lb_endereco_ip = Label(self.container3, text="Endereço IP:", font=self.fonte, width=10)
        self.lb_endereco_ip.pack(side=LEFT)

        self.txt_endereco_ip = Entry(self.container3)
        self.txt_endereco_ip["width"] = 25
        self.txt_endereco_ip["font"] = self.fonte
        self.txt_endereco_ip.pack(side=LEFT)

        self.lb_mascara_sub_rede = Label(self.container4, text="Mascara de Sub-rede :", font=self.fonte, width=10)
        self.lb_mascara_sub_rede.pack(side=LEFT)

        self.txt_mascara_sub_rede = Entry(self.container4)
        self.txt_mascara_sub_rede["width"] = 25
        self.txt_mascara_sub_rede["font"] = self.fonte
        self.txt_mascara_sub_rede.pack(side=LEFT)

        self.lb_gateway = Label(self.container5, text="Gateway Padrão:", font=self.fonte, width=10)
        self.lb_gateway.pack(side=LEFT)

        self.txt_gateway = Entry(self.container5)
        self.txt_gateway["width"] = 25
        self.txt_gateway["font"] = self.fonte
        self.txt_gateway.pack(side=LEFT)

    #-----
        self.lb_dns = Label(self.container6, text="DNS:", font=self.fonte, width=10)
        self.lb_dns.pack(side=LEFT)

        self.txt_dns = Entry(self.container6)
        self.txt_dns["width"] = 25
        self.txt_dns["font"] = self.fonte
        self.txt_dns.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirRede
        self.bntInsert.pack(side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarRede
        self.bntAlterar.pack(side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirRede
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="", font=("Verdana", "9", "italic"))
        self.lblmsg.pack()

 #--------

    def inserirRede(self):
        network = Redes()

        network.endereco_ip = self.txt_endereco_ip.get()
        network.mascara_sub_rede = self.txt_mascara_sub_rede.get()
        network.gateway = self.txt_gateway.get()
        network.dns = self.txt_dns.get()

        self.lblmsg["text"] = network.insertRedes()

        self.txt_id_rede.delete(0, END)
        self.txt_endereco_ip.delete(0, END)
        self.txt_mascara_sub_rede.delete(0, END)
        self.txt_gateway.delete(0, END)
        self.txt_dns.delete(0, END)

    def alterarRede(self):
        network = Redes()

        network.id_redes = self.txt_id_rede.get()
        network.endereco_ip = self.txt_endereco_ip.get()
        network.mascara_sub_rede = self.txt_mascara_sub_rede.get()
        network.gateway = self.txt_gateway.get()
        network.dns = self.txt_dns.get()
        network.senha = self.txtsenha.get()

        self.lblmsg["text"] = network.updateRedes()

        self.txt_id_rede.delete(0, END)
        self.txt_endereco_ip.delete(0, END)
        self.txt_mascara_sub_rede.delete(0, END)
        self.txt_gateway.delete(0, END)
        self.txt_dns.delete(0, END)
        self.txtsenha.delete(0, END)

    def excluirRede(self):
        network = Redes()

        network.id_redes = self.txt_id_rede.get()

        self.lblmsg["text"] = network.deleteRedes()

        self.txt_id_rede.delete(0, END)
        self.txt_endereco_ip.delete(0, END)
        self.txt_mascara_sub_rede.delete(0, END)
        self.txt_gateway.delete(0, END)
        self.txt_dns.delete(0, END)
        self.txtsenha.delete(0, END)


#-----
    def buscarRede(self):
        network = Redes()

        iddns = self.txt_id_rede.get()

        self.lblmsg["text"] = network.selectUser(iddns)

        self.txt_id_rede.delete(0, END)
        self.txt_id_rede.insert(INSERT, network.id_redes)

        self.txt_endereco_ip.delete(0, END)
        self.txt_endereco_ip.insert(INSERT, network.endereco_ip)

        self.txt_mascara_sub_rede.delete(0, END)
        self.txt_mascara_sub_rede.insert(INSERT, network.mascara_sub_rede)

        self.txt_gateway.delete(0, END)
        self.txt_gateway.insert(INSERT, network.gateway)

        self.txt_dns.delete(0, END)
        self.txt_dns.insert(INSERT, network.dns)

        self.txtsenha.delete(0, END)
        self.txtsenha.insert(INSERT, network.senha)

root = Tk()
Application(root)
root.mainloop()
