from tkinter import *
from tkinter import messagebox
from customtkinter import *
import  register as reg


#import validation as val
class login():
    def __init__(self,INTER):
        super().__init__()
        #ANCHO=1920
        #ALTO=800
        #POSX=-10
        #POSY=-1
        #PosisionX="+"+str(POSX)
        #PosisionY="+"+str(POSY)
        #ANCHOALTO=str(ANCHO)+"x"+str(ALTO)
        #self.interfaz =INTER                        #Declara la ventana principal, donde se dibujara todo que es igual al parametro que crea la ventana
        #self.interfaz.title("Login")                #Declara el titulo que se muestra Arriba de la Ventana
        #self.interfaz.geometry(ANCHOALTO+PosisionX+PosisionY)          #Declara el tamaño , ancho y largo de la ventana
        #self.interfaz.configure(bg_color="#303030")
        self.user=StringVar()                            #Variable que tomara el valor del Usuario y lo convertira en String 
        self.password=StringVar()                        #Variable que tomara el valor de la Contraseña y lo convertira en String
        self.regis=reg.register(INTER)
        #self.validation=vali()
        #self.dibujarVentana()


    def dibujarVentana(self,ruta):
        self.LoginFrame=CTkFrame(ruta,
                                 width=1920,
                                 height=800,
                                 bg_color="#7f8c8d",
                                 fg_color="#7f8c8d"
                                 )
        self.LoginFrame.pack()
        
        #
        
        self.WorkForm=CTkFrame(self.LoginFrame,
                               width=500,
                               height=500,
                               bg_color="#403930",
                               border_color="#e47d00",
                               border_width=4,
                               fg_color="#303030",
                               )
        self.WorkForm.place(x=450,y=150)
        self.formulario()

#-------------------------------Area de las funciones BackEnd--------------------------------------------------------------------------
    def inicio(self):
          u="admin"
          p="admin"
          if self.user.get()==u and self.password.get()==p:
                self.LoginFrame.pack_forget()

          else:
                messagebox.showerror("Error","Usuario o contraseña incorrectos")

    def registro(self):
            self.regis.dibujarVentana(self.LoginFrame)







#=====================================================================================================================================
#=================================Area del diseño del formularioo o espacio de ingreso de datos========================================

    def formulario(self):
#-------------------------------------label del titulo de inicio de sesion-----------------------------------------------------
      #---------------------------Frame de fonde del Label de Titulo------------------------------------------------------------
            self.marco=CTkFrame(self.WorkForm,
                                    width=350,
                                    height=40,
                                    bg_color="#403930",
                                    border_color="#c0392b",
                                    border_width=4,
                                    fg_color="#303030",
                               )
            self.marco.place(x=80,y=10)
      
      #============================================================================================================================
      #---------------------------Label que esta dentro del Frame marco del Titulo de Inicio de Sesion-----------------------------------------------------------
            CTkLabel(self.marco,text="Inicio de Sesión",
              width=40,                                                  #tamaño total para el ancho del label
              height=1,                                                  #tamaño total para la altura del label
              font=('Arial',32),                                         #tamaño de la letra y tipo de letra que estara dentro del label
              fg_color="#303030",                                        #color de fondo interno del label
              bg_color="#303030",                                        #color de fondo del label
              text_color="#e47d00",                                      #color del texto dentro del label


            #Como los Label en CTK no contienen bordes, se sustituye por el frame que lo simula
              ).place(x=10,y=10)
#=====================================================================================================================================
#------------------------------------label texto de indicacion--------------------------------------------------------------------------
            CTkLabel(self.WorkForm,text="Ingrese sus datos para Acceder Por favor: ",
                  width=35,
                  height=1,
                  font=('Arial',20),                                          #tamaño de la letra que estara dentro del label
                  fg_color="#303030",                                         #color de fondo interno del label
                  bg_color="#303030",                                         #color de fondo del label
                  text_color="#e47d00"
              ).place(x=10,y=98)
#==========================================================================================================================================
#------------------------------------ingreso de usuario--------------------------------------------------------------------------
            CTkLabel(self.WorkForm,
                  text="usuario:",
                  width=8,
                  height=3,
                  font=('Arial',30),                                          #tamaño de la letra que estara dentro del label
                  fg_color="#303030",                                         #color de fondo interno del label
                  bg_color="#303030",                                         #color de fondo del label
                  text_color="#e47d00"
              ).place(x=68,y=160)

            CTkEntry(self.WorkForm,
                  width=180,
                  fg_color="#3A3636",
                  font=CTkFont(size=20),
                  text_color="#E67428",
                  border_color="#ff6600",
                  textvariable=self.user
              ).place(x=180,y=163)
#==========================================================================================================================================
#--------------------------------Ingreso de contraseña-----------------------------------------------------------------------------------
            CTkLabel(self.WorkForm,
                  text="Contraseña:",
                  width=10,
                  height=3,
                  font=('Arial',30),                                          #tamaño de la letra que estara dentro del label
                  fg_color="#303030",                                         #color de fondo interno del label
                  bg_color="#303030",                                         #color de fondo del label
                  text_color="#e47d00"
              ).place(x=10,y=260)

            CTkEntry(self.WorkForm,
                  width=180,
                  fg_color="#3A3636",
                  font=CTkFont(size=20),
                  text_color="#E67428",
                  border_color="#ff6600",
                  textvariable=self.password
              ).place(x=180,y=263)
#========================================================================================================================================
#------------------------------------boton de inicio de sesion--------------------------------------------------------------------------
            CTkButton(
                  self.WorkForm,
                  text="Iniciar Sesión",
                  width=180,
                  height=3,
                  font=('Arial',20),                                          #tamaño de la letra que estara dentro del label
                  bg_color="#f1c40f",
                  fg_color="#f1c40f",
                  text_color="#424949",
                  hover_color="#e67e22",
                  command=self.inicio
            ).place(x=60,y=400)
#=====================================================================================================================================
#------------------------------------boton de Registro--------------------------------------------------------------------------
            CTkButton(
                  self.WorkForm,
                  text="Registrarse",
                  width=180,
                  height=3,
                  font=('Arial',20),                                          #tamaño de la letra que estara dentro del label
                  bg_color="#f1c40f",
                  fg_color="#f1c40f",
                  text_color="#424949",
                  hover_color="#e67e22",
                  command=self.registro
            ).place(x=260,y=400)
#=====================================================================================================================================
#========================================================================================================================================
#objeto = login(CTk())
#objeto.interfaz.mainloop()