import mysql.connector as puente

class db:
    def __init__(self):
        self.cursor=""
        self.conexion=""

    def conectar(self):
        self.conexion=puente.connect(
        host="localhost",
        user="root",
        password="",
        database="ediLszonepruebas")
        self.cursor=self.conexion.cursor()
        #self.cursor.close()
        #self.conexion.close()


