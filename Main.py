#En pocas palabras, el código para abrir una ventana (desde "from" hasta ".mainloop()")
#Librería para la interfaz
from tkinter import * 
from Administrador import *
from Usuario import *
from Sucursal import *
from Productos import *

import json

admin = Administrador()

def loguearse_action(): # usen snake_case po pollos
    if usuario() in admin.usuarios:
        if contrasenia() == admin.usuarios[usuario()].get_password():
            print("LOGUEADOOOOOOO PAAAAA")
        else:
            print("CONTRA INCORRECTA")
    else:
        print("Usuario no encontrado")

def usuario():
    return usuario_textbox.get()

def contrasenia():
    return password_textbox.get()

def registrarse_action():
    admin.registrarUsuario(usuario(), contrasenia())


root = Tk() 

root.title("Inventario") 
root.iconbitmap("0_Ico.ico")
root.iconbitmap("0_Ico.ico") #no me esta funcando
root.geometry("720x480") #Tamaño estándar de la ventana 

lbl_usuario = Label(root, text="Usuario") #Las siguientes dos líneas mostrar texto
lbl_usuario.pack()

usuario_textbox = Entry(root, width=24) #el entry es como una caja de texto sin salto de linea
usuario_textbox.pack()

lbl_password = Label(root, text="Contraseña")
lbl_password.pack()

password_textbox = Entry(root, width=24, show="●") #el show= es para mostrar otro caracter en vez de un caracter real
password_textbox.pack()

btn = Button(root, text="Iniciar sesion", command= loguearse_action) #Botón
btn.config(bg="white", fg="black") #Dar estilo (también se puede hacer desde Button())
btn.pack()

registrarse = Button(root, text="Registrarse", command= registrarse_action)
registrarse.config(bg="white", fg="black")
registrarse.pack(side=RIGHT)

root.mainloop() #Comienza el loop