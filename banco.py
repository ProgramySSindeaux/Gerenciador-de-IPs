#IMPORTANDO MODULO DE SQlite
import sqlite3

class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS redes (
                     id_redes INTEGER PRIMARY KEY AUTOINCREMENT,
                     endreco_ip TEXT,
                     mascara_sub_rede TEXT,
                     gateway TEXT,
                     dns TEXT)""")
        self.conexao.commit()
        c.close()
