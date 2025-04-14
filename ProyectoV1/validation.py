import index as root
from customtkinter import *

class validation:
    def __init__(self):
        super().__init__()
        self.estado=False
        self.direction=root.APP(CTk())
    
    def vali1(self):
        if self.estado==True:
           self.direction.val1=True
           self.direction.validation2()
    