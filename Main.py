#En pocas palabras, el código para abrir una ventana (desde "from" hasta ".mainloop()")
#Librería para la interfaz
from tkinter import * 

def myFunction(): # usen snake_case po pollos
    print("Leo pollo")
    print("usuario: " + get_username())
    print("contra super secreta: " + get_password())

def get_username():
    return usuario_textbox.get()

def get_password():
    return password_textbox.get()

def registrarse_action():
    print("benja weno pal ñacson te tiro to'o el pixi")


root = Tk() 

root.title("Inventario") 
#root.iconbitmap("0_Ico.ico") #no me esta funcando
root.geometry("720x480") #Tamaño estándar de la ventana 

lbl_usuario = Label(root, text="Usuario") #Las siguientes dos líneas mostrar texto
lbl_usuario.pack()

usuario_textbox = Entry(root, width=24) #el entry es como una caja de texto sin salto de linea
usuario_textbox.pack()

lbl_password = Label(root, text="Contraseña")
lbl_password.pack()

password_textbox = Entry(root, width=24, show="●") #el show= es para mostrar otro caracter en vez de un caracter real
password_textbox.pack()

btn = Button(root, text="Iniciar sesion", command= myFunction) #Botón
btn.config(bg="white", fg="black") #Dar estilo (también se puede hacer desde Button())
btn.pack()

registrarse = Button(root, text="Registrarse", command= registrarse_action)
registrarse.config(bg="white", fg="black")
registrarse.pack(side=RIGHT)

root.mainloop() #Comienza el loop