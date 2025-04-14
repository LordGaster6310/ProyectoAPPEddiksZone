from customtkinter import *
from tkinter import *
from tkinter import ttk
import login as lg

class validation():
    def __init__(self):
        self.val=False
       
    def action(self):
        if self.val==True:
            print("interconectado")
#log=lg.login(CTk())
#reg=rg.register(CTk())
class APP():
    def __init__(self, INTER):
        super().__init__()
        #self.root = INTER
        self.log=lg.login(INTER)
        ANCHO=1920
        ALTO=800
        POSX=-10
        POSY=-1
        PosisionX="+"+str(POSX)
        PosisionY="+"+str(POSY)
        ANCHOALTO=str(ANCHO)+"x"+str(ALTO)
        self.interfaz =INTER                      #Declara la ventana principal, donde se dibujara todo que es igual al parametro que crea la ventana
        self.interfaz.title("EDIKSZONE")                #Declara el titulo que se muestra Arriba de la Ventana
        self.interfaz.geometry(ANCHOALTO+PosisionX+PosisionY)          #Declara el tamaño , ancho y largo de la ventana
        self.interfaz.configure(bg_color="#303030")
        self.SuperFrame()
        self.val1=False

        #self.login=self.log.dibujarVentana()
    def validationI(self,res):
            self.val1=res
            self.validation2()
    def validation2(self):
        if self.val1==True:
            print("validado corectamente")
        else:
            print("falla de validacion")
    def SuperFrame(self):
       
        self.Container=CTkFrame(self.interfaz,
                 width=1920,
                 height=800,
                 bg_color="#303030",
                 fg_color="#ff0000"
                 ).place(x=0,y=0)
        CTkLabel(self.Container,
                 text="hola en la app",
                 width=420,
                 height=15,
                 font=('Arial',20)
                 ).place(x=500,y=400)
        self.login=self.log.dibujarVentana(self.Container)
        


    
app=APP(CTk())
app.interfaz.mainloop()


