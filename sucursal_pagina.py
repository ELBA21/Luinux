from tkinter import *

root = Tk()

root.geometry("720x480")
root.title("Sucursales")

# Función de agregar (en proceso)
def agregar():
    print("Agregar")

# Función de modificar (en proceso)
def modificar():
    print("Modificar")

# Función de eliminar (en proceso)
def eliminar():
    print("Eliminar")

# Función de ingresar (en proceso)
def ingresar():
    print("Ingresar")    

#Todos los frames a utilizar 
frame1 = Frame(root)
frame1.pack(pady=10)
frame2 = Frame(root)
frame2.pack(pady=10)
frame3 = Frame(root)
frame3.pack(pady=10)
frame4 = Frame(root)
frame4.pack(pady=10)
frame5 = Frame(root)
frame5.pack(pady=10)
label = Label(frame1, text="Sucursales", font="Helvetica 15")
label.pack(pady=20)

#Botones (después los pongo con for)
btn1 = Button(frame2, text="Agregar", padx=5, pady=2, command=agregar, bg= "lightgrey")
btn2 = Button(frame2, text="Modificar", padx=5, pady=2, command=modificar, bg= "lightgrey")
btn3 = Button(frame2, text="Eliminar", padx=5, pady=2, command=eliminar, bg= "lightgrey")

btn1.grid(row=0, column=0, padx=5)
btn2.grid(row=0, column=1, padx=5)
btn3.grid(row=0, column=2, padx=5)

#Listbox
listbox_sucursal = Listbox(frame3, width=40, height=12)
listbox_sucursal.pack()

#===================Placeholder========================
def onFocusIn(event):
    if buscar_sucursal.get() == 'Buscar':
        buscar_sucursal.delete(0, END)
        buscar_sucursal.config(fg='black')

def onFocusOut(event):
    if buscar_sucursal.get() == '':
        buscar_sucursal.insert(0, 'Buscar')
        buscar_sucursal.config(fg='grey')

buscar_sucursal = Entry(frame4, width=25)
buscar_sucursal.insert(0, 'Buscar')
buscar_sucursal.bind('<FocusIn>', onFocusIn)
buscar_sucursal.bind('<FocusOut>', onFocusOut)
buscar_sucursal.config(fg='grey')
buscar_sucursal.pack()
#======================================================

#Último botón
btn4 = Button(frame5, text="Ingresar", padx=5, command=ingresar, bg= "lightgrey")
btn4.pack()

root.mainloop()
