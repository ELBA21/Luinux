from tkinter import *
from Productos import Productos
from Sucursal import Sucursal
from string import *
import Agregar
import Editar
##Cosas temporales


#===================== Crear la ventana principal
root = Tk()
root.geometry("480x480")
root.title("Lista de Productos")
#====================================

surcursal_provisoria = Sucursal(1)
surcursal_provisoria.productos = {}

#=========================Metodo para botones
def abrirAgregar():
       Agregar.abrirAgregar(root, surcursal_provisoria, listBoxProductos) #Insertamos las clases a llamar en los metodos
       actualizar_productos()                                            #Asi evitamos importaciones circulares
def abrir_Editar():
       Editar.abrir_Editar(root, surcursal_provisoria, listBoxProductos, SelecProducto)
       actualizar_productos()

def eliminar_Producto():
       id_producto = SelecProducto()
       posicion_producto = listBoxProductos.curselection()
       if id_producto:
              surcursal_provisoria.eliminar_producto(id_producto)
              listBoxProductos.delete(posicion_producto)
              SelecProducto()
       else:
              print("No hay elemento seleccionado")

def buscar_producto():
       search = text_box_busqueda.get()
       productos = listBoxProductos.get(0, END)
       productos_array = list(productos)
       n = 0
       print("buscando " + search)
       for producto in productos_array:
              if str(search) in producto:
                     listBoxProductos.select_clear(0, END)
                     listBoxProductos.select_set(n)
                     print(search + "encontrado")
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


                #==========================Elementos de la malla
                #=======================================

lbl_iniciar = Label(frame_0, text="PRODUCTOS", font="Helvetica 15")
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
BotonVender = Button(mallaDeBotones, text="Vender", bg= "lightgrey", borderwidth=1, relief="solid")
BotonVender.grid(row=0, column=3, padx=4)

#=======================================

#===================Labels De Informacion
mallaDeLabels = Frame(frame_1, borderwidth=1, relief="solid")
mallaDeLabels.grid(row=2, column=0, pady=10)

LabelInformacion = Label(mallaDeLabels,text="Información del Producto:")
LabelInformacion.grid(row=5, column=0)
labelNombre = Label(mallaDeLabels, text="Nombre del Producto:")
labelNombre.grid(row=6, column=0, padx=100)
labelId = Label(mallaDeLabels, text="ID del Producto")
labelId.grid(row=7, column=0)
label_precio_compra = Label(mallaDeLabels, text="Precio de Compra:")
label_precio_compra.grid(row=8, column=0)
labelPrecio = Label(mallaDeLabels, text="Precio de Venta:")
labelPrecio.grid(row=9, column=0)
labelCantidad = Label(mallaDeLabels, text="Cantidad del Producto:")
labelCantidad.grid(row=10, column=0)

#============================================



#=============================================



def SelecProducto(event=None): #Ponerle el none, sirve para que no deba necesariamente tener una entrada.
       indice = listBoxProductos.curselection()
       if indice:
              i = indice[0]
              string = listBoxProductos.get(i)
              producto_nombre, id_producto = string.split()
              
              producto = surcursal_provisoria.get_producto(id_producto)
              if producto:
                     print(f"Nombre {producto.nombre}, Id: {producto.id} Precio: {producto.precio_venta}, Stock: {producto.stock} ")
                     labelNombre.config(text=f"Nombre del Producto: {producto.nombre}")
                     labelId.config(text=f"Id del Producto: {producto.id}")
                     label_precio_compra.config(text=f"Precio de Compra: {producto.precio_compra}")
                     labelPrecio.config(text=f"Precio de Venta: {producto.precio_venta}")
                     labelCantidad.config(text=f"Stock del Producto: {producto.stock}")
                     return id_producto
              else:
                     print("No se encuentra")
       else:
              labelNombre.config(text=f"Nombre del Producto: ")
              labelId.config(text=f"Id del Producto: ")
              label_precio_compra.config(text=f"Precio de Compra: ")
              labelPrecio.config(text=f"Precio de Venta: ")
              labelCantidad.config(text=f"Stock del Producto: ")
              print("No hay producto seleccionado")

#===========================================


listBoxProductos.bind("<<ListboxSelect>>", SelecProducto)
def actualizar_productos():
       listBoxProductos.delete(0, END)

       for key, producto in surcursal_provisoria.productos.items():
            StringUnica = producto.nombre + " " + producto.id 
            listBoxProductos.insert(END, StringUnica)
            #Tuve que concatenarlas porque si se colocan por separado abajo cambia de tipo, pasa de ser String a tupla. Y es paja trabajar :p

root.mainloop()
