#En pocas palabras, el código para abrir una ventana (desde "from" hasta ".mainloop()")
#Librería para la interfaz
from tkinter import * 

def myFunction():
    print("Agustín pollo")

root = Tk() 

root.title("Inventario") 
root.iconbitmap("0_Ico.ico")
root.geometry("720x480") #Tamaño estándar de la ventana

lbl = Label(root, text="Hola :D") #Las siguientes dos líneas mostrar texto
lbl.pack()

btn = Button(root, text=":0", command= myFunction) #Botón
btn.config(bg="black", fg="red") #Dar estilo (también se puede hacer desde Button())
btn.pack()

root.mainloop() #Comienza el loop