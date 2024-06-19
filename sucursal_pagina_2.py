from tkinter import *
from Usuario import Usuario
import paginaProductos

from Main import admin
from Main import guardar

def buscar_sucursal_func():
    return

def abrir_sucursal():
    return

def abrir_usuario(nombre):
    usuario = admin.getUsuario(nombre)

    def actualizar_sucursales():
        listbox_sucursal.delete(0,END)
        lista_aux=[]
        for key,sucursal in usuario.sucursales.items():
            lista_aux.append(f"{key}") #No se como cresta esto funciono, no pregunten
        lista_aux.sort()
        listbox_sucursal.insert(END, *lista_aux)

    def selec_sucursal(event =None):
        indice = listbox_sucursal.curselection()
        if indice:  
            string = listbox_sucursal.get(indice)
            sucursal = usuario.get_sucursal(string)
            if sucursal:
                print("sucursal_pagina -> selec_sucursal")
                print(f"Nombre + {sucursal.get_nombre()}")
                return string
            
    def eliminar_sucursal():
        if selec_sucursal() == None:
            print("No se ha seleccionado nada")
        else:
            sucursal_seleccionada = usuario.sucursales[selec_sucursal()]
            usuario.eliminar_sucursal(sucursal_seleccionada.get_nombre())
            guardar(admin)  
            actualizar_sucursales()

    def modificar():
        if selec_sucursal() == None:
            print("sucursal_pagina -> modificar: No se selecciono producto")
        else:
            sucursal_seleccionada = usuario.sucursales[selec_sucursal()]
            top2 = Toplevel()
            top2.geometry("360x240")
            top2.title("Modificar Sucursal")
            frame1_modificar = Frame(top2)
            frame1_modificar.pack(pady=10)
            label_modificar = Label(frame1_modificar, text= "Modificar sucursal", font="Helvetica 15")
            label_modificar.pack(pady=10)
            entry_modificar = Entry(frame1_modificar, borderwidth=1, relief="solid")
            entry_modificar.pack(pady=10)
            nombre_antiguo =sucursal_seleccionada.get_nombre()
            def guardar_cambios(a):
                usuario.cambiar_nombre_sucursal(entry_modificar.get(), nombre_antiguo)
                guardar(admin)    
                actualizar_sucursales()
                top2.destroy()

            frame_botones = Frame(frame1_modificar)
            frame_botones.pack(pady=10)
            boton_guardar_modificar = Button(frame_botones, text="Guardar",command=lambda:guardar_cambios(nombre_antiguo), bg="lightgrey", borderwidth=1, relief="solid" )
            boton_guardar_modificar.pack(pady=5)
            boton_cerrar_modificar = Button(frame_botones,text="Cerrar", command=lambda:top2.destroy(),bg="lightgrey", borderwidth=1,relief="solid")
            boton_cerrar_modificar.pack(padx=4)

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
        def agregar_listbox():
            if nombre_sucursal.get():
                usuario.crear_sucursal(nombre_sucursal.get())
                guardar(admin)
                actualizar_sucursales()
                top1.destroy()
            else:
                print("texto vacio")
            
        #Boton Agregar
        btn_agregar = Button(frame3_agregar, text="Crear",command=agregar_listbox, bg= "lightgrey", borderwidth=1, relief="solid", width=6, height=1)
        btn_agregar.pack()
        btn_cerrar = Button(frame3_agregar, text="Cerrar", command=cerrar_agregar, bg= "grey", borderwidth=1, relief="solid" )
        btn_cerrar.pack(pady=10)
        #Esto es para que funcione el botón con la tecla "Enter"
        nombre_sucursal.bind("<Return>", lambda event: btn_agregar.invoke())

    root = Tk()

    root.geometry("480x480")
    root.title("Sucursales")

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
    listbox_sucursal.bind("<<ListboxSelect>>", selec_sucursal)

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

    actualizar_sucursales()


    root.mainloop()