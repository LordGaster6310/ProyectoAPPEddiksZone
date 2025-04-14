import Bd as dataBase

class crud(dataBase.db):
    def __init__(self):
        self.idCont_dia=""
        self.consolaEle=""
        self.juegoEle=""
        self.tiempoEle=""
        self.precio=""


    def listar(self):
        query="SELECT * FROM contabilidad_diaria"
        self.cursor.execute(query)
        contenido=self.cursor.fetchall()
        return contenido

    def ingresar(self):
        query=f"insert into contabilidad_diaria(consolaEle,juegoEle,precio,tiempoEle)value ('{self.consolaEle}','{self.juegoEle}',{self.precio},{self.tiempoEle})"
        self.cursor.execute(query) #pedimos al cursor que ejecute el codigo sql
        self.conexion.commit() #confirmacion que deseo ejecutar el sql

        contador=self.cursor.rowcount #rowcount cuenta las filas afectadas en el sql anterior´
        print ("se agrego ", contador," juego")

        #print(f"se podria agregar '{self.consolaEle}','{self.juegoEle}',{self.precio},{self.tiempoEle}")

    def editar(self):
        query=f'UPDATE contabilidad_diaria SET consolaEle="{self.consolaEle}", juegoEle="{self.juegoEle}", precio="{self.precio}",tiempoEle="{self.tiempoEle}" WHERE idCont_Dia={self.idCont_dia}'

        self.cursor.execute(query)
        self.conexion.commit()
        contador=self.cursor.rowcount
        print("se edito ", contador," juego")