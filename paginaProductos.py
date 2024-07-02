from tkinter import *
from tkinter import messagebox
from Productos import Productos
from Sucursal import Sucursal
from string import *
from Main import admin
from Main import guardar
import Agregar
import Editar
##Cosas temporales
def abrir_pagina_productos(pagina_sucursales, sucursal_llamada):
       #Creacion de pagina
       pagina_sucursales.withdraw()
       root = Toplevel(pagina_sucursales)
       root.geometry("480x600")
       root.title(f"{sucursal_llamada.nombre}")
       root.grab_set()
       root.focus()
       #sucursal_llamada.productos = {} AWEONAOS ESTABAN BORRANDO LA WEA
       def actualizar_productos():
              print("Tesot1")
              listBoxProductos.delete(0, END)
              lista_aux = []
              print("Test2")
              for key, producto in sucursal_llamada.productos.items():
                     print("test3")
                     StringUnica = producto.nombre + " " + producto.id 
                     lista_aux.append(str(StringUnica))
                     #Tuve que concatenarlas porque si se colocan por separado abajo cambia de tipo, pasa de ser String a tupla. Y es paja trabajar :p
              lista_aux.sort() #ordenamos la lista
              listBoxProductos.insert(END, *lista_aux) #el diccionario sigue "desordenado" pero visualmente se  ve alfabeticamente ordenado
       def SelecProducto(event=None): #Ponerle el none, sirve para que no deba necesariamente tener una entrada.
              indice = listBoxProductos.curselection()
              if indice:
                     i = indice[0]
                     string = listBoxProductos.get(i)
                     producto_nombre, id_producto = string.split()
                     producto = sucursal_llamada.get_producto(id_producto)

                     if producto:
                            print(f"Nombre {producto.nombre}, ID: {producto.id} Precio: {producto.precio_venta}, Stock: {producto.stock} ")
                            labelNombre.config(text=f"Nombre del producto: {producto.nombre}")
                            labelId.config(text=f"ID del producto: {producto.id}")
                            label_precio_compra.config(text=f"Precio de compra: {producto.precio_compra}")
                            labelPrecio.config(text=f"Precio de venta: {producto.precio_venta}")
                            labelCantidad.config(text=f"Stock del producto: {producto.stock}")
                            return id_producto
                     else:
                            root.grab_set()
                            messagebox.showerror("Error", "No se encuentra")
                            root.grab_release()
                            print("No se encuentra")
                            return None
              else:
                     labelNombre.config(text=f"Nombre del producto: ")
                     labelId.config(text=f"ID del producto: ")
                     label_precio_compra.config(text=f"Precio de compra: ")
                     labelPrecio.config(text=f"Precio de venta: ")
                     labelCantidad.config(text=f"Stock del producto: ")
                     messagebox.showerror("Error", "No se ha seleccionado ningun producto")
                     root.grab_release()
                     return None
       def abrirAgregar():
              Agregar.abrirAgregar(root, sucursal_llamada, listBoxProductos)
              actualizar_productos()
       def abrir_Editar():
              if SelecProducto() != None: #hacemos esto para no abrir una ventana vacia a la hora de editar
                     Editar.abrir_Editar(root, sucursal_llamada, listBoxProductos, SelecProducto())
                     actualizar_productos()
       def eliminar_Producto():
              id_producto = SelecProducto()
              posicion_producto = listBoxProductos.curselection()
              if id_producto:
                     sucursal_llamada.eliminar_producto(id_producto)
                     listBoxProductos.delete(posicion_producto)
                     guardar(admin)
                     SelecProducto()
              else:
                     messagebox.showerror("Error", "No has seleccionado un elemento!")
                     print("No hay elemento seleccionado")
       def volver_a_sucursales():
              guardar(admin)
              root.destroy()
              pagina_sucursales.deiconify()
       root.protocol("WM_DELETE_WINDOW", volver_a_sucursales)
       def buscar_producto():
              search = text_box_busqueda.get()
              productos = listBoxProductos.get(0, END)
              productos_array = list(productos)
              n = 0
              print("Buscando " + search)
              for producto in productos_array:  #busqueda
                     if str(search) in producto: #si el string se encuentra en la lista seleccionara la primera coincidencia
                            listBoxProductos.select_clear(0, END)
                            listBoxProductos.select_set(n)
                            print(search + " encontrado") 
                            break
                     n = n+1
       #=======================Malla para organizar
       frame_0 = Frame(root)
       frame_0.pack()
       frame_listbox = Frame(root)
       frame_listbox.pack(pady=(50,5))
       frame_search = Frame(root)
       frame_search.pack(pady=(4,4))
       frame_botones = Frame(root)
       frame_botones.pack()
       frame_1 = Frame(root)
       frame_1.pack()
       #=============================================================

       lbl_iniciar = Label(frame_0, text="Productos", font="Helvetica 15")
       lbl_iniciar.pack(pady=(70,0))
       #================ListBox=====
       listBoxProductos = Listbox(frame_listbox, width=50, height=10, borderwidth=1, relief="solid")
       listBoxProductos.pack()
       grid_busqueda = Frame(frame_search, bd=2)
       grid_busqueda.grid(row=1, column=0)
       text_box_busqueda = Entry(grid_busqueda, width=40, borderwidth=1, relief="solid")
       text_box_busqueda.grid(row=0, column=0)
       boton_search = Button(grid_busqueda, text="Buscar", command=buscar_producto, bg = "lightgrey", borderwidth=1, relief="solid")
       boton_search.grid(row=0, column=1, padx= 4)
       #==========================

       #==============================Botones
       mallaDeBotones = Frame(frame_botones, bd=2)
       mallaDeBotones.grid(row=1, column=0)
       botonAgregar = Button(mallaDeBotones, text="Agregar", command=abrirAgregar, bg= "lightgrey", borderwidth=1, relief="solid")
       botonAgregar.grid(row=0,column=0, padx=4)
       botonEditar = Button(mallaDeBotones, text="Editar", command= abrir_Editar, bg= "lightgrey", borderwidth=1, relief="solid")
       botonEditar.grid(row=0, column=1, padx=4)
       BotonEliminar = Button(mallaDeBotones, text="Eliminar", command= eliminar_Producto, bg= "lightgrey", borderwidth=1, relief="solid")
       BotonEliminar.grid(row=0, column=2, padx=4)
       BotonVender = Button(mallaDeBotones, text="Cerrar",command=volver_a_sucursales ,bg= "lightgrey", borderwidth=1, relief="solid")
       BotonVender.grid(row=0, column=3, padx=4)
       #=======================================

       #===================Labels De Informacion 
       mallaDeLabels = Frame(frame_1, borderwidth=1, relief="solid")
       mallaDeLabels.grid(row=2, column=0, pady=10)
       LabelInformacion = Label(mallaDeLabels,text="Información del producto:")
       LabelInformacion.grid(row=5, column=0)
       labelNombre = Label(mallaDeLabels, text="Nombre del producto:")
       labelNombre.grid(row=6, column=0, padx=100)
       labelId = Label(mallaDeLabels, text="ID del producto:")
       labelId.grid(row=7, column=0)
       label_precio_compra = Label(mallaDeLabels, text="Precio de compra:")
       label_precio_compra.grid(row=8, column=0)
       labelPrecio = Label(mallaDeLabels, text="Precio de venta:")
       labelPrecio.grid(row=9, column=0)
       labelCantidad = Label(mallaDeLabels, text="Cantidad del producto:")
       labelCantidad.grid(row=10, column=0)
       #============================================
       listBoxProductos.bind("<<ListboxSelect>>", SelecProducto)

       actualizar_productos()

       root.mainloop()
