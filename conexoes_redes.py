import sqlite3
from banco import Banco

class Redes(object):
    def __init__(self, id_redes=0, endereco_ip="", mascara_sub_rede="", dns="",
                 gateway=""):
        self.info = {}
        self.id_redes = id_redes
        self.endereco_ip = endereco_ip
        self.mascara_sub_rede = mascara_sub_rede
        self.gateway = gateway
        self.dns = dns

    def insertRede(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute("INSERT INTO redes (endereco_ip, mascara_sub_rede, gateway, dns) VALUES (?, ?, ?, ?)",
                      (self.endereco_ip, self.mascara_sub_rede, self.gateway, self.dns))

            banco.conexao.commit()
            c.close()

            return "Configuração de rede cadastrada com sucesso!"
        except sqlite3.Error:
            return "Ocorreu um erro na inserção das configurações de rede"

    def updateRede(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute("UPDATE redes SET endereco_ip = ?, mascara_sub_rede = ?, gateway = ?, dns = ? WHERE id_redes = ?",
                      (self.endereco_ip, self.mascara_sub_rede, self.gateway, self.dns, self.id_redes))

            banco.conexao.commit()
            c.close()

            return "Configuração de rede atualizada com sucesso!"
        except sqlite3.Error:
            return "Ocorreu um erro na alteração das configurações de rede"
#-------------------------------------------------------------
#-----
def deleteRede(self):
    banco = Banco()
    try:
        c = banco.conexao.cursor()

        c.execute("DELETE FROM redes WHERE endereco_ip = ?", (self.endereco_ip,))

        banco.conexao.commit()
        c.close()

        return "Configurações de rede excluídas com sucesso!"
    except sqlite3.Error:
        return "Ocorreu um erro na exclusão das configurações de rede"

#-------------------------------------------------------------
def selectNetwork (self, id_redes):
    banco = Banco()
    try:
        c = banco.conexao.cursor()

        c.execute("SELECT * FROM dnss WHERE iddns = ?", (id_redes,))

        for linha in c:
            self.id_redes = linha[0]
            self.endereco_ip = linha[1]
            self.mascara_sub_rede = linha[2]
            self.gateway = linha[3]
            self.dns = linha[4]

        c.close()

        return "Busca feita com sucesso!"
    except sqlite3.Error:
        return "Ocorreu um erro na busca das configurações de rede"
