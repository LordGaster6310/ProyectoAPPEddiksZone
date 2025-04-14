from tkinter import *
from tkinter import messagebox
from customtkinter import *
from tkinter import ttk
class register():
    def __init__(self,INTER):
        super().__init__()
        ANCHO=1920
        ALTO=800
        POSX=-10
        POSY=-1
        PosisionX="+"+str(POSX)
        PosisionY="+"+str(POSY)
        ANCHOALTO=str(ANCHO)+"x"+str(ALTO)
        self.interfaz =INTER                                            #Declara la ventana principal, donde se dibujara todo que es igual al parametro que crea la ventana
        self.interfaz.title("Login")                                    #Declara el titulo que se muestra Arriba de la Ventana
        self.interfaz.geometry(ANCHOALTO+PosisionX+PosisionY)           #Declara el tamaño , ancho y largo de la ventana
        self.interfaz.configure(bg_color="#303030")
        self.user=StringVar()                                           #Variable que tomara el valor del Usuario y lo convertira en String 
        self.password=StringVar()                                       #Variable que tomara el valor de la Contraseña y lo convertira en String
        self.cp=StringVar()
        self.email=StringVar()
        self.phone=StringVar()
        #self.dibujarVentana()


    def dibujarVentana(self,posision):
        self.WorkForm=CTkFrame(posision,
                               width=900,
                               height=500,
                               bg_color="#403930",
                               border_color="#e47d00",
                               border_width=4,
                               fg_color="#303030",
                               )
        self.WorkForm.place(x=350,y=150)
        self.formulario()
    def  eliminarVentana(self):
          self.WorkForm.destroy()
#-------------------------------Area de las funciones BackEnd--------------------------------------------------------------------------
#--------------------------------funcion para crear los labels  y entrys ingresandoles el texto y las posiciones de en donde se posicionara-----
    def labelsForm(self,texto,px,py):
            CTkLabel(self.WorkForm,text=f"{texto}",
                  width=35,                                             #tamaño total para el ancho del label
                  height=1,                                             #tamaño total para la altura del label
                  font=('Arial',30),                                    #tamaño de la letra y tipo de letra que estara dentro del label
                  fg_color="#303030",                                   #color de fondo interno del label
                  bg_color="#303030",                                   #color de fondo del label
                  text_color="#e47d00"                                  #color del texto dentro del label
              ).place(x=px,y=py)
      
    def entryForm(self,texto,px,py,tv):
          self.a=CTkEntry(self.WorkForm,                                      #en donde se ubocara el entry
                  placeholder_text=texto,                               #texto de ejemplo
                  placeholder_text_color="#a6a6a6",                     #color del texto de ejemplo
                  width=180,                                            #anho del entry
                  fg_color="#3A3636",                                   #color de la letra que se ingresa
                  font=CTkFont(size=20),                                #tamanño de letra que se ingrese
                  text_color="#E67428",                                 #color del texto que se ingresa
                  border_color="#ff6600",                               #color del borde del entry
                  textvariable=tv
              ).place(x=px,y=py)                                        #px=cordenadas eje x, py=cordenadas en ejey donde se ubicara el entry

    def pruevas(self):
          us=self.user.get()
          ps=self.password.get()
          cp=self.cp.get()
          
          print("datos: "+us+"+"+ps+"+"+cp)



#=====================================================================================================================================
#=================================Area del diseño del formularioo o espacio de ingreso de datos========================================

    def formulario(self):
#-------------------------------------label del titulo de inicio de sesion-----------------------------------------------------
      #---------------------------Frame de fonde del Label de Titulo------------------------------------------------------------
            self.marco=CTkFrame(self.WorkForm,
                                    width=550,
                                    height=45,
                                    bg_color="#403930",
                                    border_color="#c0392b",
                                    border_width=4,
                                    fg_color="#303030",
                               )
            self.marco.place(x=80,y=10)
      
      #============================================================================================================================
      #---------------------------Label que esta dentro del Frame marco del Titulo de Inicio de Sesion-----------------------------------------------------------
            CTkLabel(self.marco,text="Registro de nueva cuenta",
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
            CTkLabel(self.WorkForm,text="Ingrese sus datos para Registrarse Por favor: ",
                  width=35,
                  height=1,
                  font=('Arial',20),                                          #tamaño de la letra que estara dentro del label
                  fg_color="#303030",                                         #color de fondo interno del label
                  bg_color="#303030",                                         #color de fondo del label
                  text_color="#e47d00"
              ).place(x=10,y=98)
#==========================================================================================================================================
#------------------------------------ingreso de usuario--------------------------------------------------------------------------
            self.labelsForm("Usuario:",208,140)
            self.pr=self.entryForm("User1",320,143,self.user)

#==========================================================================================================================================
#--------------------------------Ingreso de contraseña-----------------------------------------------------------------------------------
            self.labelsForm("Contraseña:",150,180)
            self.entryForm("password",320,183,self.password)

#========================================================================================================================================
#--------------------------------Confirmacion de contraseña-----------------------------------------------------------------------------------
            self.labelsForm("Confirmar Contraseña:",10,220)
            self.entryForm("password",320,223,self.cp)

#========================================================================================================================================
#--------------------------------Correo-----------------------------------------------------------------------------------
            self.labelsForm("Correo:",217,260)
            self.entryForm("user@gmail.com",320,263,self.email)

#========================================================================================================================================
#--------------------------------Telefono-----------------------------------------------------------------------------------
            self.labelsForm("Telefono:",192,300)
            self.entryForm("04241234567",320,303,self.phone)

#========================================================================================================================================
#------------------------------------boton de inicio de sesion--------------------------------------------------------------------------
            CTkButton(
                  self.WorkForm,
                  text="regresar",
                  width=180,
                  height=3,
                  font=('Arial',20),                                          #tamaño de la letra que estara dentro del label
                  bg_color="#f1c40f",
                  fg_color="#f1c40f",
                  text_color="#424949",
                  hover_color="#e67e22",
                  command=self.eliminarVentana
            ).place(x=30,y=450)
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
                  command=self.pruevas
            ).place(x=700,y=450)
#=====================================================================================================================================
#========================================================================================================================================

#registro = register(CTk())
#registro.interfaz.mainloop()