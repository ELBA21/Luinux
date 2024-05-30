from tkinter import *
from Usuario import Usuario

root = Tk()

root.geometry("480x480")
root.title("Sucursales")
# Definición de la clase Sucursal
class Sucursal:
    def __init__(self, nombre):
        self.nombre = nombre
usuario_provisorio =  Usuario("Nombre Usuario", "Contra Usuario")
usuario_provisorio.sucursales = {}

def abrir_sucursal():
    print("Nelson")

def buscar_sucursal_func():
       search = buscar_sucursal.get()
       sucursales = listbox_sucursal.get(0, END)
       sucursales_array = list(sucursales)
       n = 0
       print("Buscando " + search)
       for sucursal in sucursales_array:  #busqueda
              if str(search) in sucursales_array: #si el string se encuentra en la lista seleccionara la primera coincidencia
                     listbox_sucursal.select_clear(0, END)
                     listbox_sucursal.select_set(n)
                     print(search + " encontrado") 
                     break
              n = n+1
#===============Función de agregar===============
#Función y ventana emergente :D
def agregar():
    top1 = Toplevel()
    top1.geometry("360x180")
    top1.title("Agregar sucursal")
    top1.focus()
    top1.grab_set()
    #Frames para Organizar    
    frame1_agregar = Frame(top1)
    frame1_agregar.pack(pady=10)
    frame2_agregar = Frame(top1)
    frame2_agregar.pack(pady=10)
    frame3_agregar = Frame(top1)
    frame3_agregar.pack()
    #Labels de Texto
    label1_agregar = Label(frame1_agregar, text= "Agregar sucursal", font="Helvetica 15").pack()
    label2_agregar = Label(frame2_agregar, text= "Nombre").grid(row=0, column=0, pady=10)
    nombre_sucursal = Entry(frame2_agregar, borderwidth=1, relief="solid")
    nombre_sucursal.grid(row=0, column=1, pady=10)
    def cerrar_agregar():
        print("Se cierra agregar_sucursal")
        top1.destroy()
    #La siguiente función es para almacenar lo escrito por la entrada a la listbox
    def agregar_listbox():
        nombre = nombre_sucursal.get()
        if nombre in usuario_provisorio.sucursales:
            print("sucursal_pagina -> agregar_listbox")
            print("Ya existe un elemento con ese nombre")
        else:
            usuario_provisorio.crear_sucursal(nombre)
            listbox_sucursal.insert(END, nombre)
            nombre_sucursal.delete(0, END)
            cerrar_agregar()
        cerrar_agregar()    
    #Boton Agregar
    btn_agregar = Button(frame3_agregar, text="Crear",command=agregar_listbox, bg= "lightgrey", borderwidth=1, relief="solid", width=6, height=1)
    btn_agregar.pack()
    btn_cerrar = Button(frame3_agregar, text="Cerrar", command=cerrar_agregar, bg= "grey", borderwidth=1, relief="solid" )
    btn_cerrar.pack(pady=10)
    #Esto es para que funcione el botón con la tecla "Enter"
    nombre_sucursal.bind("<Return>", lambda event: btn_agregar.invoke())
#====================================================================================
# Función de modificar (en proceso)
def modificar():

    top2 = Toplevel()
    top2.geometry("360x240")
    top2.title("Modificar Sucursal")
    frame1_modificar = Frame(top2)
    frame1_modificar.pack(pady=10)
    label_modificar = Label(frame1_modificar, text= "Modificar sucursal", font="Helvetica 15").pack()

# Función de eliminar
def eliminar_sucursal():
    seleccion = listbox_sucursal.curselection()
    string_Sucursal = selec_Sucursal()
    if seleccion:
        indice = seleccion[0]
        if usuario_provisorio.sucursales:  # Verificar si la lista no está vacía
            usuario_provisorio.eliminar_sucursal(string_Sucursal)
            listbox_sucursal.delete(indice)
        else:
            print("La lista de sucursales está vacía.")


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
#=

#Label para el Titutlo
label = Label(frame1, text="Sucursales", font="Helvetica 15")
label.pack(pady=20)

#Botones (después los pongo con for)
btn1 = Button(frame2, text="Agregar", padx=5, pady=2, command=agregar, bg= "lightgrey", borderwidth=1, relief="solid").grid(row=0, column=0, padx=5)
btn2 = Button(frame2, text="Modificar", padx=5, pady=2, command=modificar, bg= "lightgrey", borderwidth=1, relief="solid").grid(row=0, column=1, padx=5)
btn3 = Button(frame2, text="Eliminar", padx=5, pady=2, command=eliminar_sucursal, bg= "lightgrey", borderwidth=1, relief="solid").grid(row=0, column=2, padx=5)

#Listbox
listbox_sucursal = Listbox(frame3, width=40, height=12, borderwidth=1, relief="solid")
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
buscar_grid = Frame(frame4, bd=2)
buscar_grid.pack()
buscar_sucursal = Entry(buscar_grid, width=25, borderwidth=1, relief="solid")
buscar_sucursal.insert(0, 'Buscar')
buscar_sucursal.bind('<FocusIn>', onFocusIn)
buscar_sucursal.bind('<FocusOut>', onFocusOut)
buscar_sucursal.config(fg='grey')
buscar_sucursal.grid(row=0, column=0)
buscar_boton = Button(buscar_grid, text="Buscar", command=buscar_sucursal_func, padx=5, bg="lightgrey", borderwidth=1, relief="solid")
buscar_boton.grid(row=0, column=1)
#======================================================

#Último botón
btn4 = Button(frame5, text="Ingresar", command=abrir_sucursal, padx=5, bg= "lightgrey", borderwidth=1, relief="solid")
btn4.pack()

def selec_Sucursal(event = None):
    indice = listbox_sucursal.curselection()
    if indice:
        i = indice[0]
        string = listbox_sucursal.get(i)
        sucursal = usuario_provisorio.get_sucursal(string)
        if sucursal:
            print("sucursal_pagina -> selec_Sucursal " + string)
            return string
        else: 
            print("No se encuentra")            
    else:
        print("No hay nada seleccionado")



root.mainloop()
