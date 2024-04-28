from tkinter import *

root = Tk()

root.geometry("480x480")
root.title("Sucursales")

# Función de agregar (en proceso)
def agregar():
    top1 = Toplevel()
    top1.geometry("360x240")
    top1.title("Agregar sucursal")

    frame1_agregar = Frame(top1)
    frame1_agregar.pack(pady=10)
    frame2_agregar = Frame(top1)
    frame2_agregar.pack(pady=10)
    frame3_agregar = Frame(top1)
    frame3_agregar.pack()

    label1_agregar = Label(frame1_agregar, text= "Agregar sucursal", font="Helvetica 15").pack()
    label2_agregar = Label(frame2_agregar, text= "Nombre").grid(row=0, column=0, pady=10)
    nombre_sucursal = Entry(frame2_agregar).grid(row=0, column=1, pady=10)

    btn_agregar = Button(frame3_agregar, text="Crear", bg= "lightgrey").pack()


# Función de modificar (en proceso)
def modificar():
    top2 = Toplevel()
    top2.geometry("360x240")
    top2.title("Modificar sucursal")
    frame1_modificar = Frame(top2)
    frame1_modificar.pack(pady=10)
    label_modificar = Label(frame1_modificar, text= "Modificar sucursal", font="Helvetica 15").pack()

# Función de eliminar (en proceso)
def eliminar():
    top3 = Toplevel()
    top3.geometry("360x240")
    top3.title("Eliminar sucursal")
    frame1_eliminar = Frame(top3)
    frame1_eliminar.pack(pady=10)
    label_eliminar = Label(frame1_eliminar, text= "Eliminar sucursal", font="Helvetica 15").pack()

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
btn1 = Button(frame2, text="Agregar", padx=5, pady=2, command=agregar, bg= "lightgrey").grid(row=0, column=0, padx=5)
btn2 = Button(frame2, text="Modificar", padx=5, pady=2, command=modificar, bg= "lightgrey").grid(row=0, column=1, padx=5)
btn3 = Button(frame2, text="Eliminar", padx=5, pady=2, command=eliminar, bg= "lightgrey").grid(row=0, column=2, padx=5)

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
btn4 = Button(frame5, text="Ingresar", padx=5, command=ingresar, bg= "lightgrey").pack()

root.mainloop()
